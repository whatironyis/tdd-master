from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import *
from lists.models import jobs
from lists.models import donejob
from superlists import settings
from .forms import PostForm
import json

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
def home_page(request, name='1'):
    items = jobs.objects.all().filter(group=name)
    done = donejob.objects.all()
    username = None
    if request.user.is_authenticated():
        username = request.user.username
        group = Group.objects.all()
    return render_to_response('home.html', {'items': items, 'user' : username, 'group':group, 'done':done })

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

def edit(request):
    value = request.POST.get("value")
    b = jobs.objects.get(id=str(value))
    b.flag = 'done'
    b.save()
    #resp = json.dumps(b)
    return HttpResponse()

def todo(request):
    value = request.POST.get("value")
    b = jobs.objects.get(id=str(value))
    b.flag = 'todo'
    b.save()
    #resp = json.dumps(b)
    return HttpResponse()

def inpro(request):
    value = request.POST.get("value")
    b = jobs.objects.get(id=str(value))
    b.flag='wip'
    b.save()
    return HttpResponse()
#
# def one(request):
#     name = request.POST.get("name")
#     return HttpResponseRedirect('home_page', {'name': name})