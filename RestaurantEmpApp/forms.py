# RestaurantEmpApp/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class EmployeeLoginForm(AuthenticationForm):
    username = forms.CharField(label="従業員ID")  # username に employee_id を使う場合
    password = forms.CharField(label="パスワード", widget=forms.PasswordInput)
