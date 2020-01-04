from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.text import slugify

class AbstractProfile(models.Model):
    user = models.ForeignKey(User,
                             related_name='%(class)s_related',
                             on_delete=models.CASCADE)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    phone = PhoneNumberField(blank=True, unique=True)
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    class Meta:
        abstract = True

    def __str__(self):
        return "{} {}".format(self.first_name,
                               self.last_name)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(AbstractProfile, self).save(*args, **kwargs)

class Customer(AbstractProfile):
    # order = models.ForeignKey('Order',
    #                           related_name='customers',
    #                           on_delete=models.SET_NULL,
    #                           blank=True,
    #                           null=True)
    pass

class Executer(AbstractProfile):
    description = models.CharField(max_length=250)
