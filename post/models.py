
import os
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

def create_path(instance, filename):
    return os.path.join(
        instance.author.username,
        str(instance.pk),
        filename
    )

class Post(models.Model):
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name='author_post',
        on_delete=models.CASCADE,
    )
    image = models.ImageField(verbose_name=_('Post Image'), upload_to=create_path)
    title = models.CharField(verbose_name=_('Head line'), max_length=200)
    post_date = models.DateTimeField(
        verbose_name=_('Post Submitted'), auto_now_add=True)
    slug = models.SlugField(max_length=200, blank=True)
    body = models.TextField(verbose_name='Post body')

    def __str__(self):
        return self.title

    def get_upload_to(self):
        return 'photos/%d' % self.pk

    def save(self, *args, **kwargs):
        if self.pk is None:
            saved_image = self.image
            self.image = None
            super(Post, self).save(*args, **kwargs)
            self.image = saved_image
            if 'force_insert' in kwargs:
                kwargs.pop('force_insert')
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        pass
