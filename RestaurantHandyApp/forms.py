# RestaurantEmpApp/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from RestaurantEmpApp.models import Employee
from django.core.exceptions import ValidationError

class EmployeeLoginForm(AuthenticationForm):
    employee_id = forms.CharField(label="従業員ID")
    shop_id = forms.CharField(label="店舗ID")
    password = forms.CharField(label="パスワード", widget=forms.PasswordInput)

    def clean(self):
        employee_id = self.cleaned_data.get('employee_id')
        shop_id = self.cleaned_data.get('shop_id')
        password = self.cleaned_data.get('password')

        if employee_id and shop_id and password:
            try:
                user = Employee.objects.get(username=employee_id, shop_id=shop_id)
            except Employee.DoesNotExist:
                raise ValidationError('従業員IDまたは店舗IDが正しくありません。')
            if not user.check_password(password):
                raise ValidationError('パスワードが正しくありません。')
            self.user_cache = user
        else:
            raise ValidationError('全ての項目を入力してください。')
        return self.cleaned_data

    def get_user(self):
        return getattr(self, 'user_cache', None)