from django.urls import path
from .views import IndexView  # クラスをインポート

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
