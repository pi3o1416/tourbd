from django.shortcuts import render
from django.views import View
from django.contrib.auth import login, authenticate, views as auth_views
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from .forms import UserCreateForm
from .mixins import IsAnonymous


class MyLoginView(IsAnonymous, auth_views.LoginView):
    template_name = 'account/login.html'


class MyLogoutView(auth_views.LogoutView):
    template_name = 'account/logout.html'


class CreateAccount(IsAnonymous, View):
    form = UserCreateForm
    template_name = 'account/create_account.html'

    def __init__(self):
        self.form = UserCreateForm()

    def get(self, request):
        return render(request, self.template_name, {'user_create_form': self.form})

    def post(self, request):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password2')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user=user)
            else:
                raise ValidationError(
                    message='Validation Fail',
                    code='validation_fail',
                )
            return HttpResponseRedirect(reverse('general:home'))
        return self.get(request)
