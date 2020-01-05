from django.db import models
from profiles.models import Customer, Executer
from django.utils.text import slugify
from django.urls import reverse

class Order(models.Model):
    customer = models.ForeignKey(Customer,
                                related_name='orders',
                                on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    text = models.TextField()
    image = models.ImageField(upload_to='orders/%Y/%m/%d',
                                blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    executer = models.ForeignKey(Executer,
                                related_name='orders',
                                on_delete=models.SET_NULL,
                                blank=True,
                                null=True)
    condition = models.BooleanField(default=False)
    condition_success = models.BooleanField(default=False)
    moderation = models.BooleanField(default=False)
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def approv(self, executer_app):
        self.executer = executer_app
        self.condition = True
        self.save()

    def get_absolute_url(self):
        return reverse('order:order_detail',
                        kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Order, self).save(*args, **kwargs)

class ResponseOrder(models.Model):
    title = models.CharField(max_length=250)
    order = models.ForeignKey(Order,
                              related_name='responses_orders',
                              on_delete=models.CASCADE)
    executer = models.ForeignKey(Executer,
                                 related_name='responses_orders',
                                 on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    condition = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     if not self.executer:
    #         executer = Executer.objects.get(user=request.user)
    #     super(ResponseOrder, self).save(*args, **kwargs)
