
from django.contrib.auth.backends import BaseBackend
from account.models import CustomUser

class MyAuthentication(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = CustomUser.objects.get(email=email)
            pwd_valid = user.check_password(password)
            if user.is_active and pwd_valid:
                return user
        except:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None



