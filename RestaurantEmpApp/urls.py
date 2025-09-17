from django.urls import path
from .views import IndexView, EditEmployeeView  # EditEmployeeView を忘れずにインポート

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('EditEmployee/', EditEmployeeView.as_view(), name='EditEmployee'),
]
