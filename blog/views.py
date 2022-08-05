from django.shortcuts import render,get_object_or_404
from blog.models import Post
# Create your views here.
def blog_view(request , **kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        posts = Post.objects.filter(category__name = kwargs['cat_name'])
    if kwargs.get('author_username') != None :
        posts = posts.filter(author__username = kwargs['author_username'])
    context = {'posts':posts}
    return render(request,'blog/blog-home.html' , context)
def blog_single(request , pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts , pk=pid , status =1)
    context = {'post':post}
    return render(request,'blog/blog-single.html' , context)

def blog_categories(request,cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html' , context)