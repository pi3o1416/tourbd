from django.shortcuts import render
from django.views import View
from django.urls import reverse, reverse_lazy
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.contrib.auth import login, authenticate, views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import UserCreateForm, UserEditForm
from .mixins import IsAnonymous
from .models import CustomUser


class MyLoginView(IsAnonymous, auth_views.LoginView):
    template_name = 'account/login.html'


class MyLogoutView(auth_views.LogoutView):
    template_name = 'account/logout.html'


class MyPasswordChange(auth_views.PasswordChangeView):
    template_name = 'account/password_change.html'
    success_url = reverse_lazy('account:password_change_done')


class MyPasswordChangeDone(auth_views.PasswordChangeDoneView):
    template_name = 'account/password_change_done.html'


class MyPasswordReset(auth_views.PasswordResetView):
    template_name = 'account/password_reset_form.html'
    email_template_name = 'account/password_reset_email.html'
    success_url = reverse_lazy('account:password_reset_done')


class MyPasswordResetDone(auth_views.PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'


class MyPasswordResetConfirm(auth_views.PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'


class MyPasswordResetComplete(auth_views.PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'


class CreateAccount(IsAnonymous, View):
    form = UserCreateForm
    template_name = 'account/create_account.html'

    def __init__(self):
        #        self.form = self.form()
        self.form = UserCreateForm()

    def get(self, request, error=None):
        return render(request, self.template_name, {'user_create_form': self.form, 'error': error})

    def post(self, request):
        form = UserCreateForm(request.POST)
#        form = self.form(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password2')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user=user)
            else:
                raise ValidationError(
                    message='Login Fail',
                    code='login_fail',
                )
            return HttpResponseRedirect(reverse('general:home'))
        return HttpResponse(reverse('account:create_account'))


class UpdateProfile(LoginRequiredMixin, View):
    form = UserEditForm
    User = get_user_model()
    template_name = 'account/edit_account.html'

    def get(self, request):
        try:
            user = self.User.objects.get(username=request.user.username)
            self.form = UserEditForm(instance=user)
#            self.form = self.form(instance=user)
            return render(request, self.template_name, {'user_edit_form': self.form})
        except self.User.DoesNotExist:
            return HttpResponseNotFound(render(request, 'does_not_exist.html'))

    def post(self, request):
        try:
            instance = self.User.objects.get(username=request.user.username)
            form = UserEditForm(instance=instance, data=request.POST)
#            form = self.form(instance=instance, data=request.POST)
            if form.is_valid():
                password = form.cleaned_data.get('password')
                if instance.check_password(password):
                    form.save()
                    messages.success(request, 'Successfully update Profile')
                    return HttpResponseRedirect(reverse('account:edit_profile'))
                else:
                    messages.error(request, 'Incorrect Password')
                    messages.error(request, 'Failed to update Profile')
                    return HttpResponseRedirect(reverse('account:edit_profile'))
            else:
                messages.error(request, "Failed to Update Profile")
                return HttpResponseRedirect(reverse('account:edit_profile'))
        except self.User.DoesNotExist:
            return HttpResponseNotFound(render(request, 'does_not_exist.html'))
