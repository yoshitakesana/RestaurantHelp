from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .models import Employee
from .forms import EmployeeLoginForm


# ログインページ
class EmployeeLoginView(LoginView):
    template_name = 'RestaurantEmpApp/login.html'
    authentication_form = EmployeeLoginForm
    
    def get_success_url(self):
        return reverse_lazy('menu')

#社員さんのメニューページ
class MenuView(TemplateView):
    template_name='RestaurantEmpApp/menu.html'

# 従業員編集(UpdateView)
class EditEmployeeView(UpdateView):
    model = Employee
    fields = ['name', 'shop_id', 'role']
    template_name = 'RestaurantEmpApp/EditEmployee.html'
    success_url = reverse_lazy('menu')

class AddEmployeeView(CreateView):
    model = Employee
    fields = ['username', 'password', 'name', 'shop_id', 'role']
    template_name = 'RestaurantEmpApp/AddEmployee.html'
    success_url = reverse_lazy('menu')

    def form_valid(self, form):
        # パスワードをハッシュ化して保存
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return super().form_valid(form)

#従業員詳細ページ
class DetailEmployeeView(TemplateView):
    template_name='RestaurantEmpApp/DetailEmployee.html'



#メニュー編集ページ
class EditMenuView(TemplateView):
    template_name='RestaurantEmpApp/EditMenu.html'

#メニュー詳細ページ
class DetailMenuView(TemplateView):
    template_name='RestaurantEmpApp/DetailMenu.html'

#メニュー追加ページ
class AddMenuView(TemplateView):
    template_name='RestaurantEmpApp/AddMenu.html'

#社員編集ページ
class EditManagerView(TemplateView):
    template_name='RestaurantEmpApp/EditManager.html'






