from django.shortcuts import render, redirect
from .models import User, Plant
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
            return redirect('/home')
    return redirect('/')

def login(request):
    if request.method == "POST":
        user_with_email = User.objects.filter(email = request.POST['email']) 
        if user_with_email:
            user = user_with_email[0]
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id 
                return redirect('/home')
        messages.error(request, "Email or password are not correct.")
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

def home(request):
    if 'user_id' not in request.session: 
        return redirect('/')
    context={
        'current_user' : User.objects.get(id=request.session['user_id']),
    }
    return render(request, "home.html", context)


def profile(request, user_id):
    if 'user_id' not in request.session: 
        return redirect('/')
    context={
        'current_user' : User.objects.get(id = request.session['user_id']),
        # 'all_challenges': Challenge.objects.all(),
    }
    return render(request, "profile.html", context)

def edit_profile(request, user_id):
    if 'user_id' not in request.session: 
        return redirect('/')
    context={
        'current_user' : User.objects.get(id = user_id),
    }
    return render(request, "edit_profile.html", context)

def update_profile(request, user_id):
    if request.method =="POST":
        errors = User.objects.edit_validator(request.POST, user_id)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/profile/{user_id}/edit')    
        else:
            current_user = User.objects.get(id=user_id)
            current_user.first_name=request.POST['first_name']
            current_user.last_name=request.POST['last_name']
            current_user.email=request.POST['email']
            current_user.location=request.POST['location']
            current_user.save()
            messages.success(request, "You successfully updated your account.")    
        return redirect(f'/profile/{user_id}')
    

def new_note(request):
    # if 'user_id' not in request.session: 
    #     return redirect('/')
    # else: 
    return render(request, 'notes.html')


def grow(request): 
    if 'user_id' not in request.session: 
        return redirect('/')
    return render(request, 'grow.html')

def fruit_veg(request):
    # if 'user_id' not in request.session: 
    #     return redirect('/')
    context={
        'all_plants': Plant.objects.filter(category="fruit_veg"),
        'current_user' : User.objects.get(id = request.session['user_id']),
    }
    return render(request, 'fruit_veg.html', context)


def plant_details(request, plant_id):
    # if 'user_id' not in request.session: 
    #     return redirect('/')
    context={
        'current_user' : User.objects.get(id = request.session['user_id']),
        'one_plant' : Plant.objects.get(id=plant_id),
    }
    return render(request, 'plant_details.html', context)


def houseplants(request):
    # if 'user_id' not in request.session: 
    #     return redirect('/')
    context={
        'all_plants': Plant.objects.filter(category="houseplants"),
        'current_user' : User.objects.get(id = request.session['user_id']),

    }
    return render(request, 'houseplants.html', context)

def houseplant_details(request):
    return render(request, 'houseplant_details.html')

def landscaping(request):
    # if 'user_id' not in request.session: 
    #     return redirect('/')
    context={
        'all_plants': Plant.objects.filter(category="landscaping"),
        'current_user' : User.objects.get(id = request.session['user_id']),

    }
    return render(request, 'landscaping.html', context)

def herbs(request):
    # if 'user_id' not in request.session: 
    #     return redirect('/')
    context={
        'all_plants': Plant.objects.filter(category="herbs"),
        'current_user' : User.objects.get(id = request.session['user_id']),

    }
    return render(request, 'herbs.html', context)