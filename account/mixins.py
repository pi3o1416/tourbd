from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

class IsAnonymous(UserPassesTestMixin):

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse('general:home'))


