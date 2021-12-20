
from django import forms
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from .models import Post, Comment


User = get_user_model()


class FilterForm(forms.Form):
    error_message = {
        'invalid_author': 'Author does not exist',
        'invalid_date': 'Please enter a valid date',
    }
    author = forms.CharField(
        max_length=50,
        min_length=3,
        label=_('Author'),
        required=False
    )
    title = forms.CharField(
        max_length=200,
        label=_('Post title'),
        required=False,
    )
    date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'date'}),
        label=_('Date post'),
        required=False,
    )
    district = forms.CharField(
        max_length=50,
        label=_('District'),
        required=False,
    )

    def clean_author(self):
        author = self.cleaned_data.get('author')
        if author:
            try:
                User.objects.get(username=author)
            except User.DoesNotExist:
                raise forms.ValidationError(
                    self.error_message['invalid_author'],
                    code='invalid_author'
                )
        return author

    def clean_date(self):
        today = timezone.now()
        date = self.cleaned_data.get('date')
        if date:
            if date > today:
                raise forms.ValidationError(
                    self.error_message['invalid_date'],
                    code='invalid_date'
                )
        return date


class PostCreateForm(forms.ModelForm):
    body = forms.CharField(
        max_length=5000,
        label=_('Post Body'),
        widget=forms.Textarea(attrs={'class': 'textarea'})
    )
    image = forms.ImageField(
        widget=forms.FileInput(attrs={'type': 'file'})
    )
    class Meta:
        model=Post
        fields=('title', 'district', 'image', 'body')


class CommentForm(forms.ModelForm):
    comment_text = forms.CharField(label=_('Add comment'),max_length=500)
    class Meta:
        model=Comment
        fields = ('comment_text',)
