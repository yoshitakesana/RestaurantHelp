from django.urls import path
from .views import IndexView#,ListView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    #path('EditEmployee/',ListView.as_view(),name='EditEmployee'),
]
