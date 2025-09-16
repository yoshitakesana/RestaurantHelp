from django.shortcuts import render

def index(request):
	return render(request, 'RestaurantEmpApp/index.html')
