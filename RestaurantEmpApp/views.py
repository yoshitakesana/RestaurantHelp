from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from .models import Employee
from .forms import EmployeeLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import EmployeeCreateForm
from .forms import EmployeeForm

# ログインページ
class EmployeeLoginView(LoginView):
    template_name = 'RestaurantEmpApp/login.html'
    authentication_form = EmployeeLoginForm
    
    def get_success_url(self):
        return reverse_lazy('menu')

#社員さんのメニューページ
class MenuView(TemplateView):
    template_name='RestaurantEmpApp/menu.html'


# 従業員一覧(ListView)＋編集リンク
from django.views.generic import ListView

class EditEmployeeView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'RestaurantEmpApp/EditEmployee.html'
    context_object_name = 'employees'

    def get_queryset(self):
        # roleが空またはNoneの従業員のみ返す
        return Employee.objects.filter(role__isnull=True) | Employee.objects.filter(role='')

#従業員追加
class AddEmployeeView(LoginRequiredMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'RestaurantEmpApp/AddEmployee.html'
    success_url = reverse_lazy('menu')

    def get_initial(self):
        initial = super().get_initial()
        # ログインユーザー（店長）のshop_idを初期値にセット
        initial['shop_id'] = self.request.user.shop_id
        return initial

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # shop_idをreadonlyに
        form.fields['shop_id'].widget.attrs['readonly'] = True
        return form

    def form_valid(self, form):
        # shop_idを強制的に店長のshop_idに
        form.instance.shop_id = self.request.user.shop_id
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






