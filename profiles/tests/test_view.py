from django.test import TestCase
from profiles.models import Customer, Executer
from django.urls import reverse

class ExecuterListViewTest(TestCase):

    @classmethod
    def setUpTest(cls):
        number_for_customer = 13
        for customer_numb in range(number_for_customer):
            User.objects.create_user(username='user_%s' % customer_numb,
                        email='user%s@gmail.com' % customer_numb,
                        password='pass_secret')
            Customer.objects.create(user='user_%s' % customer_numb,
                        first_name='first_%s' % customer_numb,
                        last_name='last_%s' % customer_numb,
                        phone='+37525530059_%s' % customer_numb,
                        email='user_%s@gmail.com' % customer_numb)

    def test_view_url_exists_at_desired_location_customer(self):
        resp = self.client.get('/profile/customer_list/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_my_name(self):
        resp = self.client.get(reverse('profile:executer_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('profile:executer_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'profiles/manage/profile/executer_list.html')
