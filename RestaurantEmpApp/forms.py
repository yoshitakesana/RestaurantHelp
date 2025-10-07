# RestaurantEmpApp/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Employee
from django.core.exceptions import ValidationError
from .models import Food


class EmployeeLoginForm(AuthenticationForm):
    username = forms.CharField(label="従業員ID")  # username に employee_id を使う場合
    password = forms.CharField(label="パスワード", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        if username:
            try:
                user = Employee.objects.get(username=username)
                if not user.role:
                    raise ValidationError('従業員（ロール未設定）はログインできません。')
            except Employee.DoesNotExist:
                pass  # 通常の認証エラーに任せる
        return cleaned_data


class EmployeeCreateForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model=Employee
        fields=['name','password']#店舗IDは入れない
    

class EmployeeForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Employee
        # role はフォームに含めず、デフォルトは null
        fields = ['username', 'name', 'password', 'shop_id']

    # username 重複チェック
    def clean_username(self):
        username = self.cleaned_data['username']
        if Employee.objects.filter(username=username).exists():
            raise ValidationError('この username はすでに使われています。')
        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        # パスワードをハッシュ化
        user.set_password(self.cleaned_data['password'])

        # role を必ず None に設定
        user.role = None  

        if commit:
            user.save()
        return user

class FoodForm(forms.ModelForm):
    class Meta:
        model=Food
        fields=['name','price','category','image_path','is_deleted']
