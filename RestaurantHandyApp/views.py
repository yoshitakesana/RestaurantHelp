from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'RestaurantHandyApp/index.html'
    
class MainView(TemplateView):
    template_name='RestaurantHandyApp/main.html'

#ログアウトした後のページ
class Logout_successView(TemplateView):
    template_name='RestaurantHandyApp/logout_success.html'