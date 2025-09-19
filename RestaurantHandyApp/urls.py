from django.urls import path
from .views import IndexView,MainView,Logout_successView  # クラスをインポート

urlpatterns = [
    #アルバイトのログインページ
    path('', IndexView.as_view(), name='index'),
    #メインページ
    path('main/',MainView.as_view(),name='main'),
    #ログアウトしたあとのページ
    path('logout_success/',Logout_successView.as_view(),name='logout_success')
]
