# RestaurantEmpApp/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from RestaurantEmpApp.models import Employee
from django.core.exceptions import ValidationError


from django.contrib.auth import authenticate

class EmployeeLoginForm(forms.Form):
    employee_id = forms.CharField(label="従業員ID")
    shop_id = forms.CharField(label="店舗ID")
    password = forms.CharField(label="パスワード", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        employee_id = cleaned_data.get('employee_id')
        shop_id = cleaned_data.get('shop_id')
        password = cleaned_data.get('password')

        if not (employee_id and shop_id and password):
            raise ValidationError('全ての項目を入力してください。')

        user = authenticate(username=employee_id, password=password, shop_id=shop_id)
        if user is None:
            raise ValidationError('従業員ID・店舗ID・パスワードが正しくありません。')
        self.user_cache = user
        return cleaned_data

    def get_user(self):
        return getattr(self, 'user_cache', None)