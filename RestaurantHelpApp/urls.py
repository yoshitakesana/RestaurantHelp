from django.urls import path
from .views import IndexView,Food_detailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('food_detail/',Food_detailView.as_view(),name='food_detail')
]
