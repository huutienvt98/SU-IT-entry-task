from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from blog.models import Post
from django.contrib.auth.decorators import login_required
from personal.forms import PostForm
from django.utils import timezone


@login_required
def personal(request, username):
    if request.user.is_authenticated:
        username = request.user.username
    personal_posts = Post.objects.filter(author=request.user).order_by("-created_on")
    context = {
        "posts": personal_posts
    }
    
    return render(request, "personal.html", context)

def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_on = timezone.now()
            post.last_modified = timezone.now()            
            post.save()
            return redirect('personal', username=post.author)
    else:
        form = PostForm()
    return render(request, 'new_post.html', {'form': form})



# Create your views here.
