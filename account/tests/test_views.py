
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from account.models import CustomUser


class TestCreateAccount(TestCase):
    def setUp(self):
        date = timezone.datetime(year=1995, month=5, day=6).date()
        CustomUser.objects.create_user(
            username='omi',
            email='omi@gmail.com',
            password='helloworld@',
            date_of_birth=date,
            interest=['Bandarban', 'CoxBazar'],
        )
        self.data = {
            'username': ['omi99'],
            'email': ['omi99@gmail.com'],
            'password1': ['helloworld@'],
            'password2': ['helloworld@'],
            'date_of_birth': ['1999-01-01'],
            'interest': ['Bandarban', 'CoxBazar']
        }

    def test_if_url_exist_in_desire_url(self):
        response = self.client.get('/account/join/')
        self.assertEqual(response.status_code, 200)

    def test_if_url_accessable_by_name(self):
        response = self.client.get(reverse('account:create_account'))
        self.assertEqual(response.status_code, 200)

    def test_if_properly_create_account(self):

        response = self.client.post(
            reverse('account:create_account'), data=self.data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('general:home'))


class TestUpdateProfile(TestCase):
    def setUp(self):
        date = timezone.datetime(year=1995, month=5, day=6).date()
        CustomUser.objects.create_user(
            username='omi',
            email='omi@gmail.com',
            password='helloworld@',
            date_of_birth=date,
            interest=['Bandarban', 'CoxBazar'],
        )
        self.data = {
            'username': ['omi99'],
            'email': ['omi99@gmail.com'],
            'password': ['helloworld@'],
            'date_of_birth': ['1999-01-01'],
            'interest': ['Bandarban', 'CoxBazar']
        }

    def test_if_unauthorized_user_can_visit(self):
        response = self.client.get(reverse('account:edit_profile'))
        self.assertEqual(response.status_code, 302)

    def test_if_url_exist_in_desire_url(self):
        login = self.client.login(username='omi', password='helloworld@')
        response = self.client.get('/account/edit/')
        self.assertEqual(response.status_code, 200)

    def test_if_url_accessable_by_name(self):
        login = self.client.login(username='omi', password='helloworld@')
        response = self.client.get(reverse('account:edit_profile'))
        self.assertEqual(response.status_code, 200)
