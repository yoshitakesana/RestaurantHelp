from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'RestaurantHelpApp/index.html'

class Food_detailView(TemplateView):
    template_name='RestaurantHelpApp/food_detail.html'

