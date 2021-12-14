
from django.urls import path
from . import views


app_name='account'
urlpatterns = [
    path('join/', views.CreateAccount.as_view(), name='create_account'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
]
