from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
	return HttpResponse('<html><title>Listy rzeczy do zrobienia</title></html>')
def about_me_page(request):
    pass