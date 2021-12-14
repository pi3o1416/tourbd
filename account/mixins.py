from django.contrib.auth.mixins import UserPassesTestMixin

class IsAnonymous(UserPassesTestMixin):

    def test_func(self):
        return not self.request.user.is_authenticated


