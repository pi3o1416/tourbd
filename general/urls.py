
from django.urls import path
from . import views


app_name = 'general'
urlpatterns = [
    path('home/', views.HomePage.as_view(), name='home'),
]
