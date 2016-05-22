from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import *
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from lists.models import jobs
from superlists import settings
from .forms import *
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
def home_page(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username
        group = request.user.groups.all()
        items = jobs.objects.all().filter(group=group)
    return render_to_response('home.html', {'items': items, 'user' : username, 'group':group })
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def post_new(request):
    username = request.user.username
    group = request.user.groups.all()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            jobs = form.save(commit=False)
            jobs.assign = request.user
            jobs.created = timezone.now()
            jobs.finished = timezone.now()
            jobs.group = request.user.groups.all()[0]
            jobs.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'user':username,'group': group, 'form': form})

def post_detail(request, pk):
    post = get_object_or_404(jobs, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def post_edit(request, pk):
    post = get_object_or_404(jobs, pk=pk)
    group = request.user.groups.all()
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.assign = request.user
            post.created = timezone.now()
            post.finished = timezone.now()
            post.group = request.user.groups.all()[0]
            post.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm(instance=post)
        print(request.user.groups.all()[0])
    return render(request, 'post_edit.html', {'form': form, 'pk': pk, 'group': group })
@csrf_protect
def group(request):
    username = request.user.username
    group = request.user.groups.all()
    if request.method == 'POST':
        if 'add_group' in request.POST:
            form = GroupForm(request.POST)
            form1 = ChangeForm(request.POST)
            if form.is_valid():
                groups = Group.objects.get_or_create(
                name=form.cleaned_data['create_group'])
                groupy = request.POST.get("create_group")
                print (groupy)
                g = Group.objects.get(name=groupy)
                user = request.user
                user.groups.add(g)
                return HttpResponseRedirect('/group')
        if 'change_group' in request.POST:
            form1 = ChangeForm(request.POST)
            form = GroupForm(request.POST)
            if form1.is_valid():
                user = request.user
                groupa = request.POST.get("name")
                g = Group.objects.get(name=groupa)
                user.groups.clear()
                user.groups.add(g)
                return HttpResponseRedirect('/group')
    else:
        form = GroupForm()
        form1 = ChangeForm()

    return render(request, 'group.html', {'user': username, 'group': group, 'form': form,'form1': form1})
def post_delete(request):
    value = request.POST.get("value")
    b = jobs.objects.get(id=str(value))
    b.delete()
    return HttpResponseRedirect('/')

def edit(request):
    value = request.POST.get("value")
    b = jobs.objects.get(id=str(value))
    b.flag = 'done'
    b.save()
    #resp = json.dumps(b)
    # return HttpResponse()

def todo(request):
    value = request.POST.get("value")
    b = jobs.objects.get(id=str(value))
    b.flag = 'todo'
    b.save()
    #resp = json.dumps(b)
    # return HttpResponse()

def inpro(request):
    value = request.POST.get("value")
    b = jobs.objects.get(id=str(value))
    b.flag='wip'
    b.save()
    # return HttpResponse()

def delete_group(request):
    g = request.user.groups.all()[0]
    g.delete()
    user = request.user
    user.groups.clear()
    return HttpResponse()