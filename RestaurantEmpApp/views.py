from django.views.generic import TemplateView

# トップページ
class IndexView(TemplateView):
    template_name = 'RestaurantEmpApp/index.html'

# 従業員編集ページ（仮）
class EditEmployeeView(TemplateView):
    template_name = 'RestaurantEmpApp/Edit Employee.html'
