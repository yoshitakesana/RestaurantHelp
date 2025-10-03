from django.contrib.auth.backends import ModelBackend
from RestaurantEmpApp.models import Employee

class EmployeeShopBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, shop_id=None, **kwargs):
        if username is None or password is None or shop_id is None:
            return None
        try:
            user = Employee.objects.get(username=username, shop_id=shop_id)
            if user.check_password(password):
                return user
        except Employee.DoesNotExist:
            return None
        return None
