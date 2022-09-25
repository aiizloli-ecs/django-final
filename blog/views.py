from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    all_posts = Post.objects.all()
    return render(request=request,
                  template_name= "blog/home.html",
                  context={"all_posts": all_posts})
    
def post_detail(request, pk: int):
    post = Post.objects.get(pk=pk)
    return render(request=request,
                  template_name="blog/post_detail.html",
                  context={"post": post})