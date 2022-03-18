from django.shortcuts import render, redirect
from .models import User, Plant, Note, Recipe
import bcrypt
from django.contrib import messages
# from django.db.models import Count

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
        'all_notes': Note.objects.all(),
        'all_recipes': Recipe.objects.all(),
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
    if 'user_id' not in request.session: 
        return redirect('/')
    else: 
        return render(request, 'new_note.html')

def create_note(request):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method == "POST":
        current_user = User.objects.get(id = request.session['user_id'])
        Note.objects.create(
            title = request.POST['title'],
            body = request.POST['body'],
            written_by = User.objects.get(id = request.session['user_id']),
        )
    return redirect(f'/profile/{current_user.id}')

def edit_note(request, note_id):
    if 'user_id' not in request.session: 
        return redirect('/')
    else: 
        context={
            'note' : Note.objects.get(id=note_id),
        }
        return render(request, 'edit_note.html', context)

def update_note(request, note_id):
        # if request.method =="POST":
        #     errors = User.objects.edit_validator(request.POST, plant_id)
        # if len(errors) > 0:
        #     for key, value in errors.items():
        #         messages.error(request, value)
        #     return redirect(f'/plant/{plant_id}/edit')  
        # else:   
        note = Note.objects.get(id=note_id)
        note.title = request.POST['title']
        note.body = request.POST['body']
        note.save()
        current_user = User.objects.get(id = request.session['user_id'])
        messages.success(request, "Note successfully updated.")    
        return redirect(f'/profile/{current_user.id}')

def delete_note(request, note_id):
    if 'user_id' not in request.session: 
        return redirect('/')
    note=Note.objects.get(id=note_id)
    note.delete()
    current_user = User.objects.get(id = request.session['user_id'])
    return redirect(f'/profile/{current_user.id}')

def new_recipe(request):
    if 'user_id' not in request.session: 
        return redirect('/')
    else: 
        return render(request, 'new_recipe.html')

def create_recipe(request):
    if request.method == "POST":
        errors = Recipe.objects.basic_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/plant/new')
        else:   
            Recipe.objects.create(
                written_by = User.objects.get(id = request.session['user_id']),
                name = request.POST['name'],
                source = request.POST['source'],
                ingredients = request.POST['ingredients'],
                supplies = request.POST['supplies'],
                total_yield = request.POST['total_yield'],
                active_time = request.POST['active_time'],
                passive_time = request.POST['passive_time'],
                instructions = request.POST['instructions'],
            )
            current_user=User.objects.get(id = request.session['user_id'])
        return redirect(f'/profile/{current_user.id}')

def edit_recipe(request, recipe_id):
    if 'user_id' not in request.session: 
        return redirect('/')
    else: 
        context={
            'recipe' : Recipe.objects.get(id=recipe_id),
        }
        return render(request, 'edit_recipe.html', context)

def update_recipe(request, recipe_id):
    # if request.method == "POST":
        # errors = Recipe.objects.basic_validator(request.POST)
        # if len(errors)>0:
        #     for key, value in errors.items():
        #         messages.error(request,value)
    #         return redirect('/plant/new')
    # else:   
        recipe = Recipe.objects.get(id=recipe_id)
        recipe.name = request.POST['name']
        recipe.source = request.POST['source']
        recipe.ingredients = request.POST['ingredients']
        recipe.supplies = request.POST['supplies']
        recipe.total_yield = request.POST['total_yield']
        recipe.active_time = request.POST['active_time']
        recipe.passive_time = request.POST['passive_time']
        recipe.instructions = request.POST['instructions']
        recipe.save()
        current_user = User.objects.get(id = request.session['user_id'])
        messages.success(request, "Recipe successfully updated.")   
        return redirect(f'/profile/{current_user.id}')

def delete_recipe(request, recipe_id):
    if 'user_id' not in request.session: 
        return redirect('/')
    recipe=Recipe.objects.get(id=recipe_id)
    recipe.delete()
    current_user = User.objects.get(id = request.session['user_id'])
    return redirect(f'/profile/{current_user.id}')

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
            Plant.objects.create(
                category = request.POST['category'],
                name = request.POST['name'],
                plant_pic = request.POST['plant_pic'],
                latin_name = request.POST['latin_name'],
                family = request.POST['family'],
                transplant_or_ds = request.POST['transplant_or_ds'],
                start = request.POST['start'],
                succession_planting = request.POST['succession_planting'],
                spacing = request.POST['spacing'],
                height_width = request.POST['height_width'],
                companion_plants = request.POST['companion_plants'],
                dont_plant_near = request.POST['dont_plant_near'],
                sun = request.POST['sun'],
                water = request.POST['water'],
                pH = request.POST['pH'],
                soil_reqs = request.POST['soil_reqs'],
                days_to_harvest = request.POST['days_to_harvest'],
                pruning = request.POST['pruning'],
                harvesting = request.POST['harvesting'],
                common_pests = request.POST['common_pests'],
                medicinal_props = request.POST['medicinal_props'],
                edibility = request.POST['edibility'],
                other_uses = request.POST['other_uses'],
                specific_notes = request.POST['specific_notes'],
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
        plant.category = request.POST['category'],
        plant.name = request.POST['name'],
        plant.plant_pic = request.POST['plant_pic'],
        plant.latin_name = request.POST['latin_name'],
        plant.family = request.POST['family'],
        plant.transplant_or_ds = request.POST['transplant_or_ds'],
        plant.start = request.POST['start'],
        plant.succession_planting = request.POST['succession_planting'],
        plant.spacing = request.POST['spacing'],
        plant.height_width = request.POST['height_width'],
        plant.companion_plants = request.POST['companion_plants'],
        plant.dont_plant_near = request.POST['dont_plant_near'],
        plant.sun = request.POST['sun'],
        plant.water = request.POST['water'],
        plant.pH = request.POST['pH'],
        plant.soil_reqs = request.POST['soil_reqs'],
        plant.days_to_harvest = request.POST['days_to_harvest'],
        plant.pruning = request.POST['pruning'],
        plant.harvesting = request.POST['harvesting'],
        plant.common_pests = request.POST['common_pests'],
        plant.medicinal_props = request.POST['medicinal_props'],
        plant.edibility = request.POST['edibility'],
        plant.other_uses = request.POST['other_uses'],
        plant.specific_notes = request.POST['specific_notes'],
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
    # if request.method == "POST":
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

def soil(request):
    if 'user_id' not in request.session: 
        return redirect('/')
    return render(request, "soil_compost.html")

def process(request):
    if 'user_id' not in request.session: 
        return redirect('/')
    return render(request, "process.html")