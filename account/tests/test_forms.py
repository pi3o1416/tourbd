
from django.test import TestCase
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from account.models import CustomUser
from account.forms import UserCreateForm, UserEditForm


class UserCreateFormTest(TestCase):

    def form_data(self,
                  username='monir',
                  email='monir@gmail.com',
                  date_of_birth='1999-01-01',
                  interest='Bandarban, Cox-bazar, Saint-Martin, Shylet',
                  password1='helloworld@', password2='helloworld@'):
        return {
            'username': username,
            'email': email,
            'date_of_birth': date_of_birth,
            'interest': interest,
            'password1': password1,
            'password2': password2,
        }

    def test_form_with_valid_data(self):
        data = self.form_data()
        form = UserCreateForm(data)
        self.assertTrue(form.is_valid())

    def test_username_label(self):
        form = UserCreateForm()
        self.assertTrue(form.fields['username'].label == 'Username')

    def test_username_min_length(self):
        data = self.form_data(username='mo')
        form = UserCreateForm(data)
        self.assertFalse(form.is_valid())

    def test_username_max_length(self):
        data = self.form_data(username='m'*51)
        form = UserCreateForm(data)
        self.assertFalse(form.is_valid())

    def test_username_min_length_border(self):
        data = self.form_data(username='m'*3)
        form = UserCreateForm(data)
        self.assertTrue(form.is_valid())

    def test_username_max_length_border(self):
        data = self.form_data(username='m'*50)
        form = UserCreateForm(data)
        self.assertTrue(form.is_valid())

    def test_date_of_birth_label(self):
        form = UserCreateForm()
        self.assertTrue(form.fields['date_of_birth'].label == 'Date Of Birth')

    def test_date_of_birth_age_greater_than_today(self):
        data = self.form_data(
            date_of_birth=timezone.localdate() + timezone.timedelta(days=10))
        form = UserCreateForm(data)
        self.assertFalse(form.is_valid())

    def test_date_of_birth_age_less_than_15(self):
        data = self.form_data(
            date_of_birth=timezone.localdate() - timezone.timedelta(days=365*15-1))
        form = UserCreateForm(data)
        self.assertFalse(form.is_valid())

    def test_date_of_birth_age_at_15(self):
        data = self.form_data(
            date_of_birth=timezone.localdate() - timezone.timedelta(days=365*15))
        form = UserCreateForm(data)
        self.assertTrue(form.is_valid())

    def test_retype_password_equal(self):
        data = self.form_data(
            password2='helloworld2'
        )
        form = UserCreateForm(data)
        self.assertFalse(form.is_valid())

    def test_password1_label(self):
        form = UserCreateForm(self.form_data())
        self.assertTrue(form.fields['password1'].label == 'Password')

    def test_password2_label(self):
        form = UserCreateForm(self.form_data())
        self.assertTrue(
            form.fields['password2'].label == 'Password confirmation')

    def test_interest_label(self):
        form = UserCreateForm(self.form_data())
        self.assertTrue(form.fields['interest'].help_text ==
                        'Places you are interested in. comma seperated')

    def test_password2_help_text(self):
        form = UserCreateForm(self.form_data())
        self.assertTrue(form.fields['password2'].help_text ==
                        'Enter the same password as before, for verification.')


class UserEditFormTest(TestCase):
    def setUp(self):
        date = timezone.datetime(year=1995, month=5, day=6).date()
        self.user = CustomUser.objects.create_user(
            username='omi', email='omi@gmail.com', password='helloworld@', date_of_birth=date, interest=['Bandarban', 'CoxBazar'])

    def form_data(self,
                  username='omi',
                  email='omi@gmail.com',
                  date_of_birth='1995-05-06',
                  interest='Bandarban, Cox-bazar, Saint-Martin, Shylet',
                  password='helloworld@'):
        return {
            'username': username,
            'email': email,
            'date_of_birth': date_of_birth,
            'interest': interest,
            'password': password,
        }

    def test_form_with_valid_data(self):
        data = self.form_data()
        form = UserEditForm(instance=self.user, data=data)
        self.assertTrue(form.is_valid())

    def test_username_label(self):
        form = UserEditForm(instance=self.user)
        self.assertTrue(form.fields['username'].label == 'Username')

    def test_username_min_length(self):
        data = self.form_data(username='mo')
        form = UserEditForm(instance=self.user, data=data)
        self.assertFalse(form.is_valid())

    def test_username_max_length(self):
        data = self.form_data(username='m'*51)
        form = UserEditForm(instance=self.user, data=data)
        self.assertFalse(form.is_valid())

    def test_username_min_length_border(self):
        data = self.form_data(username='m'*3)
        form = UserEditForm(instance=self.user, data=data)
        self.assertTrue(form.is_valid())

    def test_username_max_length_border(self):
        data = self.form_data(username='m'*50)
        form = UserEditForm(instance=self.user, data=data)
        self.assertTrue(form.is_valid())

    def test_date_of_birth_label(self):
        form = UserEditForm(instance=self.user)
        self.assertTrue(form.fields['date_of_birth'].label == 'Date Of Birth')

    def test_date_of_birth_age_greater_than_today(self):
        data = self.form_data(
            date_of_birth=timezone.localdate() + timezone.timedelta(days=10))
        form = UserEditForm(instance=self.user, data=data)
        self.assertFalse(form.is_valid())

    def test_date_of_birth_age_less_than_15(self):
        data = self.form_data(
            date_of_birth=timezone.localdate() - timezone.timedelta(days=365*15-1))
        form = UserEditForm(instance=self.user, data=data)
        self.assertFalse(form.is_valid())

    def test_date_of_birth_age_at_15(self):
        data = self.form_data(
            date_of_birth=timezone.localdate() - timezone.timedelta(days=365*15))
        form = UserEditForm(instance=self.user, data=data)
        self.assertTrue(form.is_valid())

    def test_password1_label(self):
        form = UserEditForm(instance=self.user, data=self.form_data())
        self.assertTrue(form.fields['password'].label == 'Password')

    def test_interest_label(self):
        form = UserEditForm(instance=self.user, data=self.form_data())
        self.assertTrue(form.fields['interest'].help_text ==
                        'Places you are interested in. comma seperated')
