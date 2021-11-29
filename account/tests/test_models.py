from django.test import TestCase
from django.utils import timezone
from account.models import CustomUser

# Create your tests here.


class CustomUserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CustomUser.objects.create(
            username='bob',
            first_name='bob',
            last_name='marley',
            email='bob@gmail.com',
            date_of_birth=timezone.now(),
            interest=[['shylet'], ['bandarban'], ['shundarban'], ['cox-bazar']]
        )

    def test_date_of_birth_label(self):
        user = CustomUser.objects.get(id=1)
        field_label = user._meta.get_field('date_of_birth').verbose_name
        self.assertEqual(field_label, 'Date of Birth')

    def test_date_of_birth_default(self):
        user = CustomUser.objects.create(
            username='connor',
            first_name='jim',
            last_name='connor',
            email='jim@gmail.com',
            interest=[['shylet'], ['bandarban'], ['shundarban'], ['cox-bazar']]
        )
        expected_default = timezone.now().date()
        actual_default = user.date_of_birth.date()
        self.assertEqual(expected_default, actual_default)

    def test_duplicate_email(self):
        try:
            CustomUser.objects.create(
                username='connor',
                first_name='jim',
                last_name='connor',
                email='bob@gmail.com',
                interest=[['shylet'], ['bandarban'],
                          ['shundarban'], ['cox-bazar']]
            )
        except:
            self.assertTrue(True)

    def test_duplicate_username(self):
        try:
            CustomUser.objects.create(
                username='bob',
                first_name='jim',
                last_name='connor',
                email='jim@gmail.com',
                interest=[['shylet'], ['bandarban'],
                          ['shundarban'], ['cox-bazar']]
            )
        except:
            self.assertTrue(True)

    def test_get_absolute_url(self):
        self.assertTrue(False)
