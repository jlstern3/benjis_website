from django.shortcuts import render, redirect
from .models import User
import bcrypt
from django.contrib import messages
from django.db.models import Count

def index(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def create_user(request):
    if request.method == "POST":
        errors = User.objects.create_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/register')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                email = request.POST['email'],
                password=pw_hash,
            )
            request.session['user_id'] = user.id 
            return redirect('/main_page')
    return redirect('/')

def login(request):
    if request.method == "POST":
        user_with_email = User.objects.filter(email = request.POST['email']) 
        if user_with_email:
            user = user_with_email[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id 
                return redirect('/main_page')
        messages.error(request, "Email or password are not correct.")
    return redirect('/')

def home(request):
    return render(request, 'home.html')

def new_blog_post(request):
    # if 'user_id' not in request.session: 
    #     return redirect('/')
    # else: 
    return render(request, 'new_blog_post.html')

def grow (request): 
    return render(request, 'grow.html')

def fruit_veg(request):
    return render(request, 'fruit_veg.html')

def plant_details(request):
    return render(request, 'plant_details.html')


def houseplants(request):
    return render(request, 'houseplants.html')

def houseplant_details(request):
    return render(request, 'houseplant_details.html')

def landscaping(request):
    return render(request, 'landscaping.html')

