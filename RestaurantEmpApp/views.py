from django.views.generic import TemplateView
from django.urls import reverse_lazy


# ログインページ
class LoginView(TemplateView):
    template_name = 'RestaurantEmpApp/login.html'

#社員さんのメニューページ
class MenuView(TemplateView):
    template_name='RestaurantEmpApp/menu.html'

# 従業員編集ページ（本当はUpdateVIew）
class EditEmployeeView(TemplateView):
    template_name = 'RestaurantEmpApp/EditEmployee.html'
    ##success_url = reverse_lazy('menu')

#従業員追加ページ
class AddEmployeeView(TemplateView):
    template_name='RestaurantEmpApp/AddEmployee.html'

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






