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
            current_user.profile_pic = request.POST['profile_pic']
            current_user.save()
            messages.success(request, "You successfully updated your account.")    
        return redirect(f'/profile/{user_id}')
    

def new_note(request):
    # if 'user_id' not in request.session: 
    #     return redirect('/')
    # else: 
    return render(request, 'notes.html')

def new_plant(request):
    if 'user_id' not in request.session: 
        return redirect('/')
    else: 
        return render(request, 'new_plant.html')

def create_plant(request):
    if request.method == "POST":
        errors = Plant.objects.basic_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/plant/new')
        else:   
            plant = Plant.objects.create(
                name = request.POST['name'],
                latin_name = request.POST['latin_name'],
                sun = request.POST['sun'],
                water = request.POST['water'],
                height_width = request.POST['height_width'],
                spacing = request.POST['spacing'],
                days_to_harvest = request.POST['days_to_harvest'],
                pH = request.POST['pH'],
                planting = request.POST['planting'],
                family = request.POST['family'],
                soil_reqs = request.POST['soil_reqs'],
                companion_plants = request.POST['companion_plants'],
                dont_plant_near = request.POST['dont_plant_near'],
                pruning = request.POST['pruning'],
                harvesting = request.POST['harvesting'],
                common_pests = request.POST['common_pests'],
                medicinal_props = request.POST['medicinal_props'],
                edibility = request.POST['edibility'],
                other_uses = request.POST['other_uses'],
                specific_notes = request.POST['specific_notes'],
                category = request.POST['category'],
            )
    return redirect('/grow')

def plant_details(request, plant_id):
    # if 'user_id' not in request.session: 
    #     return redirect('/')
    context={
        'current_user' : User.objects.get(id = request.session['user_id']),
        'plant' : Plant.objects.get(id=plant_id),
    }
    return render(request, 'plant_details.html', context)

def edit_plant(request, plant_id):
    if 'user_id' not in request.session: 
        return redirect('/')
    else: 
        context={
            'plant' : Plant.objects.get(id=plant_id),
        }
        return render(request, 'edit_plant.html', context)
        
def update_plant(request, plant_id):
        # if request.method =="POST":
        #     errors = User.objects.edit_validator(request.POST, plant_id)
        # if len(errors) > 0:
        #     for key, value in errors.items():
        #         messages.error(request, value)
        #     return redirect(f'/plant/{plant_id}/edit')  
        # else:   
        plant = Plant.objects.get(id=plant_id)
        plant.name = request.POST['name']
        plant.latin_name = request.POST['latin_name']
        plant.sun = request.POST['sun']
        plant.water = request.POST['water']
        plant.height_width = request.POST['height_width']
        plant.spacing = request.POST['spacing']
        plant.days_to_harvest = request.POST['days_to_harvest']
        plant.pH = request.POST['pH']
        plant.planting = request.POST['planting']
        plant.family = request.POST['family']
        plant.soil_reqs = request.POST['soil_reqs']
        plant.companion_plants = request.POST['companion_plants']
        plant.dont_plant_near = request.POST['dont_plant_near']
        plant.pruning = request.POST['pruning']
        plant.harvesting = request.POST['harvesting']
        plant.common_pests = request.POST['common_pests']
        plant.medicinal_props = request.POST['medicinal_props']
        plant.edibility = request.POST['edibility']
        plant.other_uses = request.POST['other_uses']
        plant.specific_notes = request.POST['specific_notes']
        plant.category = request.POST['category']
        plant.save()
        messages.success(request, "Plant successfully updated.")    
        return redirect(f'/grow/details/{plant_id}')

def delete_plant(request, plant_id):
    if request.method == "POST":
        remove = Plant.objects.get(id=plant_id)
        remove.delete()
    return redirect('/grow')

def like_plant(request, plant_id):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method == "POST":
        current_user = User.objects.get(id = request.session['user_id'])
        one_plant = Plant.objects.get(id = plant_id)
        current_user.plants_liked.add(one_plant)
    return redirect(f'/profile/{current_user.id}')

def unlike_plant(request, plant_id):
    if 'user_id' not in request.session: 
        return redirect('/')
    if request.method == "POST":
        current_user = User.objects.get(id=request.session['user_id'])
        unlike_plant = Plant.objects.get(id=plant_id)
        current_user.plants_liked.remove(unlike_plant)
    return redirect(f'/profile/{current_user.id}')

def plant_search(request):
    plant_search = request.POST['plant_search']
    if len(plant_search) == 0:
        return render(request, "blank.html")
    if len(Plant.objects.filter(name__startswith = request.POST['plant_search'])) == 0:
        return render(request, "no_results.html")
    else:
        context = {
            'results': Plant.objects.filter(name__startswith = request.POST['plant_search'])
        }
    return render(request, "search_results.html", context)

def grow(request): 
    if 'user_id' not in request.session: 
        return redirect('/')
    context={
        'current_user': User.objects.get(id=request.session['user_id']),
    }
    return render(request, 'grow.html', context)

def all_plants(request):
    context={
        'all_plants': Plant.objects.all()
    }
    return render(request, 'all_plants.html', context)

def herbs(request):
    # if 'user_id' not in request.session: 
    #     return redirect('/')
    context={
        'all_plants': Plant.objects.filter(category="herbs"),
        'current_user' : User.objects.get(id = request.session['user_id']),

    }
    return render(request, 'herbs.html', context)

def fruit_veg(request):
    # if 'user_id' not in request.session: 
    #     return redirect('/')
    context={
        'all_plants': Plant.objects.filter(category="fruit_veg"),
        'current_user' : User.objects.get(id = request.session['user_id']),
    }
    return render(request, 'fruit_veg.html', context)


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

