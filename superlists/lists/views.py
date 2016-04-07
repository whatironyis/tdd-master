from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,render_to_response
from lists.models import jobs
from lists.models import donejob
from superlists import settings
from .forms import PostForm


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
    done = donejob.objects.all()
    username = None
    if request.user.is_authenticated():
        username = request.user.username
    return render_to_response('home.html', {'items': items, 'user' : username, 'done':done })

def about_me_page(request):
    pass

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            jobs = form.save(commit=False)
            jobs.assign = request.user
            jobs.created = timezone.now()
            jobs.finished = timezone.now()
            jobs.save()
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})