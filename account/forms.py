
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
from django.contrib.postgres.forms import SimpleArrayField
from django.core.exceptions import ValidationError
from .models import CustomUser


class UserCreateForm(forms.ModelForm):
    """
    Form to create new User
    """
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    username = forms.CharField(
        max_length=50,
        min_length=3,
        label=_("Username/Email"),
    )

    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type' : 'date'}))

    interest = SimpleArrayField(
        forms.CharField(
            max_length=30,
        ),
        help_text = _('Places you are interested in. comma seperated')
    )

    class Meta:
        model = CustomUser
        fields = ('username','email', 'date_of_birth', 'interest')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user




