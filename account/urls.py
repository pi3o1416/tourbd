
from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('join/', views.CreateAccount.as_view(), name='create_account'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
    path('edit/', views.UpdateProfile.as_view(), name='edit_profile'),
    path('password-change/', views.MyPasswordChange.as_view(), name='password_change'),
    path('password-change/done/', views.MyPasswordChangeDone.as_view(), name='password_change_done'),
    path('password-reset/', views.MyPasswordReset.as_view(), name='password_reset'),
    path('password-reset/done/', views.MyPasswordResetDone.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.MyPasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.MyPasswordResetComplete.as_view(), name='password_reset_complete'),
]
