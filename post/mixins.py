
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect


class MyPermissionRequiredMixin(PermissionRequiredMixin):
    def handle_no_permission(self):
        return redirect('general:no_permission')


