
from django.test import TestCase
from post.models import Post
from django.contrib.auth import get_user_model

Author = get_user_model()


class TestPost(TestCase):
    def setUp(self):
        self.user = Author.objects.create_user(
            username='rasel',
            email='rasel@gmail.com',
            password='raselrasel1',
            date_of_birth='1999-01-01',
            interest=['bandarban', 'cox-bazar']
        )

        self.post = Post.objects.create(
            author=self.user,
            title='sunshine in saint-martin',
            body='Sunshine in saint-martin',
        )

    def test_body_label(self):
        self.assertEqual(self.post._meta.get_field(
            'body').verbose_name, 'Post body')

    def test_title_label(self):
        self.assertEqual(self.post._meta.get_field(
            'title').verbose_name, 'Head line')

    def test_image_label(self):
        self.assertEqual(self.post._meta.get_field(
            'image').verbose_name, 'Post Image')

    def test_image_upload_to_path(self):
        upload_path = self.post._meta.get_field('image').upload_to
        expected_path = self.user.username + '/' + \
            str(self.post.pk) + '/' + 'test.png'
        self.assertEqual(upload_path(self.post, 'test.png'), expected_path)

    def test_post_title_max_length(self):
        self.assertTrue(self.post._meta.get_field('title').max_length == 200)

    def test_post_date_auto_now_add(self):
        self.assertTrue(self.post._meta.get_field(
            'post_date').auto_now_add == True)

    def test_get_absolute_url(self):
        self.assertFalse(True)





