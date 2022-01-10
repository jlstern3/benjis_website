from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def new_blog_post(request):
    # if 'user_id' not in request.session: 
    #     return redirect('/')
    # else: 
    return render(request, 'new_blog_post.html')

def grow (request): 
    return render(request, 'grow.html')

def plant_details(request):
    return render(request, 'plant_details.html')

def houseplant_details(request):
    return render(request, 'houseplant_details.html')

