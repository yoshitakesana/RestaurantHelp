from django.contrib.auth.backends import ModelBackend
from .models import Employee

class EmployeeIDBackend(ModelBackend):
    """従業員ログイン用：employee_id + パスワード"""
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # username が数字なら employee_id として扱う
            if username.isdigit():
                user = Employee.objects.get(employee_id=username)
                if user.check_password(password):
                    return user
        except Employee.DoesNotExist:
            return None
        return None

class AdminUsernameBackend(ModelBackend):
    """管理者ログイン用：username + パスワード"""
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Employee.objects.get(username=username)
            if user.is_superuser and user.check_password(password):
                return user
        except Employee.DoesNotExist:
            return None
        return None
