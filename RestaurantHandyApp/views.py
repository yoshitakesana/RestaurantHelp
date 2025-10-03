from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import EmployeeLoginForm

class IndexView(LoginView):
    template_name = 'RestaurantHandyApp/index.html'
    authentication_form = EmployeeLoginForm
    success_url = reverse_lazy('main')  # ログイン成功後のリダイレクト先

    def form_valid(self, form):
        from django.contrib.auth import login
        login(self.request, form.get_user())
        return super().form_valid(form)

class MainView(TemplateView):
    template_name='RestaurantHandyApp/main.html'

#ログアウトした後のページ
class Logout_successView(TemplateView):
    template_name='RestaurantHandyApp/logout_success.html'