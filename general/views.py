
from django.shortcuts import render
from django.views import View


class HomePage(View):
    template_name = 'general/home.html'

    def get(self, request):
        return render(request, self.template_name)
