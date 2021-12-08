from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def new_blog_post(request):
    # if 'user_id' not in request.session: 
    #     return redirect('/')
    # else: 
    return render(request, 'new_blog_post.html')