from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import inlineformset_factory
from datetime import date
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#View imports here
from .models import *
from .filters import CustomerFilter
from .forms import PostForm, CreateUserForm

def landingPage(request):
    context = {}
    template_name = '../templates/landingpage.html'

    return render(request, template_name, context)

def home(request):
    posts = WardrobePost.objects.all()
    page_title = "Yourdrobe"
    context = {
        'posts':posts,
        'page_title':page_title,
    }
    template_name = '../templates/home.html'

    return render(request, template_name, context)
    
def profile(request, pk):
    customer = Customer.objects.get(id=pk)
    posts = customer.wardrobepost_set.all()
    context = {
        'customer':customer,
        'posts':posts,
    }
    template_name = '../templates/profile.html'

    return render(request, template_name, context)

def discover(request):
    posts = WardrobePost.objects.all()
    tags = Tag.objects.all()
    context = {
        'posts':posts,
        'tags':tags,
    }
    template_name = '../templates/discover.html'

    return render(request, template_name, context)

def search(request):
    customers = Customer.objects.all()

    customerFilter  = CustomerFilter(request.GET, queryset=Customer.objects.all())
    # postFilter  = PostFilter(request.GET, queryset=WardrobePost.objects.all())

    customers = customerFilter.qs
    # posts = postFilter.qs
    context = {
        'customerFilter':customerFilter,
        'customers':customers
        # 'posts':posts,
    }
    template_name = '../templates/search.html'

    return render(request, template_name, context)

def post(request):
    posts = WardrobePost.objects.all()
    context = {
        'customerFilter':customerFilter,
        'postFilter':postFilter,
        'posts':posts,
    }
    template_name = '../templates/post.html'

    return render(request, template_name, context)

def createPost(request):
    customer = request.user.customer
    form = PostForm(initial={
        'customer':customer
    })

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.cleaned_data['customer'] = customer
            print(form.cleaned_data['customer'])
            form.save()
            messages.info(request, 'Post successfully created!')

            return redirect('home')

    context = {
        'form':form,
    }
    
    template_name = '../templates/crud/create-post.html'
    return render(request, template_name, context)

def deletePost(request, pk):
    post = WardrobePost.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        messages.success(request,"Your post has been deleted")
        return redirect('home')

    context = {
        'post':post,
    }
    
    template_name = '../templates/crud/delete-post.html'
    return render(request, template_name, context)

def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            messages.success(request, 'Sucessfully logged in as {}'.format(user.customer.username))

            login(request, user)
            return redirect('home')
            
        else:
            messages.error(request, 'Username or password is incorrect')


    context = {}
    template_name = '../templates/login-registration/login.html'

    return render(request, template_name, context)

def registerUserPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        username = form.data.get('username')

        if form.is_valid():
            user = form.save()
            customer = Customer.objects.create(
            user=user,
            username=username,
            )
            customer.save()

            return redirect('login')

    context = {'form':form}
    template_name = '../templates/login-registration/register.html'

    return render(request,template_name, context)

def logoutUser(request):
    customer = request.user.customer
    logout(request)
    
    return redirect('/login')