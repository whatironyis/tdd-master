from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User
from lists.models import jobs
from superlists import settings

def Login(request):
    next = request.GET.get('next','/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Inactive user")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)
    return render(request, 'login.html', {'redirect_to':next})

def Logout(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)
@login_required
def home_page(request):
    items = jobs.objects.all()
    username = None
    if request.user.is_authenticated():
        username = request.user.username
    return render_to_response('home.html', {'items': items, 'user' : username })

def about_me_page(request):
    pass