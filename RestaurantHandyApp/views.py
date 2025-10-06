
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import EmployeeLoginForm

class IndexView(TemplateView):
    template_name = 'RestaurantHandyApp/index.html'

    def get(self, request, *args, **kwargs):
        form = EmployeeLoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = EmployeeLoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
        return render(request, self.template_name, {'form': form})

class MainView(TemplateView):
    template_name='RestaurantHandyApp/main.html'

#ログアウトした後のページ
class Logout_successView(TemplateView):
    template_name='RestaurantHandyApp/logout_success.html'