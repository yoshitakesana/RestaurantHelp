from django.urls import path, reverse_lazy
from .views import (
  EmployeeLoginView,
  EditEmployeeView,
  MenuView,
  AddEmployeeView,
  DetailEmployeeView,
  DetailMenuView,
  EditManagerView,
  DeleteEmployeeView,
  FoodListView,
  food_add,
  FoodUpdateView,
  FoodDeleteView,
)
from django.views.generic.edit import UpdateView
from .models import Employee

urlpatterns = [
      #ログインページ
    path('', EmployeeLoginView.as_view(template_name='RestaurantEmpApp/login.html'), name='login'),
     # メニュー画面
    path('menu/', MenuView.as_view(), name='menu'),
  # 食べ物一覧
  path('food_list/', FoodListView.as_view(), name='food_list'),
  # 食べ物追加
  path('food_add/', food_add, name='food_add'),
  # 個別メニュー編集
  path('food_edit/<int:pk>/', FoodUpdateView.as_view(), name='food_edit'),
  path('food_delete/<int:pk>/', FoodDeleteView.as_view(), name='food_delete'),
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

  #メニュー編集ページ（一覧を使う）
  path('EditMenu/', FoodListView.as_view(), name='EditMenu'),
    #メニュー詳細ページ
    path('DetailMenu/',DetailMenuView.as_view(),name='DetailMenu'),
  #メニュー追加ページ（店長は food_add を使う）
  path('AddMenu/', food_add, name='AddMenu'),
    
    #店長編集ページ
    path('EditManager/',EditManagerView.as_view(),name='EditManager')


]
