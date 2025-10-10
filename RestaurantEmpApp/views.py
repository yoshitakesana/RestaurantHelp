

# 必要なimportを先頭にまとめる
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Employee, Food
from .forms import EmployeeLoginForm, EmployeeCreateForm, EmployeeForm, FoodForm

# --- 食べ物一覧・追加ビューを先頭に ---
class FoodListView(LoginRequiredMixin, ListView):
    model = Food
    template_name = 'RestaurantEmpApp/food_list.html'
    context_object_name = 'foods'

def food_add(request):
    shop_id = request.user.shop_id if request.user.is_authenticated else ''
    if request.method == "POST":
        form = FoodForm(request.POST, shop_id=shop_id)
        if form.is_valid():
            food = form.save(commit=False)
            food.shop_id = shop_id
            food.save()
            return redirect('food_list')
    else:
        form = FoodForm(shop_id=shop_id)
    return render(request, 'RestaurantEmpApp/food_add.html', {'form': form})


# 個別メニュー編集
from django.views.generic.edit import UpdateView
class FoodUpdateView(LoginRequiredMixin, UpdateView):
    model = Food
    form_class = FoodForm
    template_name = 'RestaurantEmpApp/food_edit.html'
    success_url = reverse_lazy('food_list')


# 食べ物削除
from django.views.generic.edit import DeleteView
class FoodDeleteView(LoginRequiredMixin, DeleteView):
    model = Food
    template_name = 'RestaurantEmpApp/food_confirm_delete.html'
    success_url = reverse_lazy('food_list')

# 従業員削除
class DeleteEmployeeView(LoginRequiredMixin, DeleteView):
    model = Employee
    template_name = 'RestaurantEmpApp/confirm_delete.html'
    success_url = reverse_lazy('EditEmployee')

# ログインページ
class EmployeeLoginView(LoginView):
    template_name = 'RestaurantEmpApp/login.html'
    authentication_form = EmployeeLoginForm

    def form_valid(self, form):
        user = form.get_user()
        # ロールが空(null/空文字)ならログイン不可
        if not user.role:
            from django.contrib.auth import logout
            logout(self.request)
            form.add_error(None, '従業員（ロール未設定）はログインできません。')
            return self.form_invalid(form)
        return super().form_valid(form)

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





#メニュー詳細ページ
class DetailMenuView(TemplateView):
    template_name='RestaurantEmpApp/DetailMenu.html'



#社員編集ページ
class EditManagerView(TemplateView):
    template_name='RestaurantEmpApp/EditManager.html'






