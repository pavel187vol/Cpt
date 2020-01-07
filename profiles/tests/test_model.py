from django.test import TestCase
from profiles.models import Executer
from django.contrib.auth.models import User
class ExecuterModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        User.objects.create_user(username='jacob',
                    email='jacob@…', password='top_secret')
        Executer.objects.create(user=user ,first_name='Big', last_name='Bob',
                    phone='375255300598', email='a-bla@gmail.com',)

    def test_first_name_label(self):
        example=Executer.objects.get(id=1)
        field_label = example._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'first name')

    def test_first_name_max_length(self):
        example=Executer.objects.get(id=1)
        max_length = example._meta.get_field('first_name').max_length
        self.assertEquals(max_length,70)

    def test_get_absolute_url(self):
        example=Executer.objects.get(id=1)
        #This will also fail if the urlconf is not defined.
        self.assertEquals(example.get_absolute_url(),
                    "/profile/executer/{}/".format(example.user.username))
