from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from blog.models import Post, Comment, Category
from blog.forms import CommentForm, CreatePost, CreateCategory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)
  

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),

    }

    return render(request, "blog/detail.html", context)
  
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
  
def test(request):
    context = {
    }
    return render(request, "blog/index.html", context)

def makepost(request):
    if request.method == "POST":
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            post = Post(
                author.request.user.username,
                title=form.cleaned_data["title"],
                body=form.cleaned_data["body"],
                image=form.cleaned_data["image"]
            )
            post.save()
            post.categories.set(form.cleaned_data["categories"])
            post.save()
            return redirect('blog_index')
    else:
        form = CreatePost()
    
    return render(request, 'blog/makepost.html', {'form': form})

def viewCategory(request):
    categories = Category.objects.all()
    form = CreateCategory()
    context = {
        'categories': categories,
    }
    return render(request, "blog/catergory_view.html", context)

def profile(request):
    posts = Post.objects.all().order_by("-created_on")
    username = request.user.username
    context = {
        "posts": posts, "username": username,
    }
    
    return render(request, "blog/profile.html", context)
  
  
class CustomLoginView(LoginView):
    template_name = 'login.html'

class CustomLogoutView(LogoutView):
    template_name = 'logged_out.html'