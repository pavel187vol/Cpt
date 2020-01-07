from django.test import TestCase
from profiles.models import Customer, Executer
from orders.models import Order
from django.contrib.auth.models import User
from django.urls import reverse

class OrderListViewTest(TestCase):

    @classmethod
    def setUp(self):
        rood = User.objects.create_user(username='rood', email='rood@gmail.com',
                    password='test_secret')
        rood.save()
        pavel = User.objects.create_user(username='pavel', email='pavel@gmail.com',
                    password='test_secret')
        pavel.save()
        customer = Customer.objects.create(user=rood,
                    first_name='first',
                    last_name='last',
                    phone='+37525530059',
                    email='user_%s@gmail.com')
        customer.save()
        executer = Executer.objects.create(user=pavel,
                    first_name='first',
                    last_name='last',
                    phone='+37525530059',
                    email='user_%s@gmail.com')
        executer.save()
        order = Order.objects.create(customer=customer, title='Order title',
                    text='Order text', price=140)
        order.save()

    def test_view_url_exists_at_desired_location_order(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)

    def test_view_reverse_url_exists_at_desired_location_order(self):
        resp = self.client.get(reverse('order:order_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_reverse_url_exists_at_desired_location_template_order(self):
        resp = self.client.get(reverse('order:order_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'orders/manage/order/order_list.html')

class OrderDetailViewTest(TestCase):

    @classmethod
    def setUp(self):
        rood = User.objects.create_user(username='rood', email='rood@gmail.com',
                    password='test_secret')
        rood.save()
        pavel = User.objects.create_user(username='pavel', email='pavel@gmail.com',
                    password='test_secret')
        pavel.save()
        customer = Customer.objects.create(user=rood,
                    first_name='first',
                    last_name='last',
                    phone='+37525530059',
                    email='user_%s@gmail.com')
        customer.save()
        executer = Executer.objects.create(user=pavel,
                    first_name='first',
                    last_name='last',
                    phone='+37525530059',
                    email='user_%s@gmail.com')
        executer.save()
        order = Order.objects.create(customer=customer, title='Order title',
                    text='Order text', price=140)
        order.save()

    def test_view_url_exists_at_desired_location_order_detail(self):
        order = Order.objects.get(id=1)
        resp = self.client.get('/order/{}/'.format(order.slug))
        self.assertEqual(resp.status_code, 200)

    # def test_view_reverse_url_exists_at_desired_location_order_detail(self):
    #     order = Order.objects.get(id=1)
    #     resp = self.client.get(reverse('order:order_detail'))
    #     self.assertEqual(resp.status_code, 200)

class OrderCreateViewTest(TestCase):

    @classmethod
    def setUp(self):
        rood = User.objects.create_user(username='rood', email='rood@gmail.com',
                    password='test_secret')
        rood.save()
        pavel = User.objects.create_user(username='pavel', email='pavel@gmail.com',
                    password='test_secret')
        pavel.save()
        customer = Customer.objects.create(user=rood,
                    first_name='first',
                    last_name='last',
                    phone='+37525530059',
                    email='user_%s@gmail.com')
        customer.save()
        executer = Executer.objects.create(user=pavel,
                    first_name='first',
                    last_name='last',
                    phone='+37525530059',
                    email='user_%s@gmail.com')
        executer.save()
        order = Order.objects.create(customer=customer, title='Order title',
                    text='Order text', price=140)
        order.save()

    def
