from django.urls import path, reverse_lazy
from .views import EmployeeLoginView, EditEmployeeView, MenuView,AddEmployeeView,DetailEmployeeView,EditMenuView,DetailMenuView,AddMenuView,EditManagerView, DeleteEmployeeView
from django.views.generic.edit import UpdateView
from .models import Employee

urlpatterns = [
      #ログインページ
    path('', EmployeeLoginView.as_view(template_name='RestaurantEmpApp/login.html'), name='login'),
     # メニュー画面
    path('menu/', MenuView.as_view(), name='menu'), 
     # 従業員編集画面
  path('EditEmployee/', EditEmployeeView.as_view(), name='EditEmployee'),
  # 個別従業員編集ページ
  path('EditEmployee/<int:pk>/', UpdateView.as_view(model=Employee, fields=['name', 'shop_id', 'role'], template_name='RestaurantEmpApp/EditEmployeeDetail.html', success_url=reverse_lazy('EditEmployee')), name='EditEmployeeDetail'),
  # 従業員削除
  path('DeleteEmployee/<int:pk>/', DeleteEmployeeView.as_view(), name='DeleteEmployee'),
    #従業員追加画面
    path('AddEmployee/',AddEmployeeView.as_view(),name='AddEmployee'),
    #選択した従業員の詳細画面
    path('DetailEmployee/',DetailEmployeeView.as_view(),name='DetailEmployee'),

    #メニュー編集ページ
    path('EditMenu/',EditMenuView.as_view(),name='EditMenu'),
    #メニュー詳細ページ
    path('DetailMenu/',DetailMenuView.as_view(),name='DetailMenu'),
    #メニュー追加ページ
    path('AddMenu/',AddMenuView.as_view(),name='AddMenu'),
    
    #店長編集ページ
    path('EditManager/',EditManagerView.as_view(),name='EditManager')


]
