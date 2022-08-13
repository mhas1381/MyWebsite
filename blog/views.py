from django.shortcuts import render,get_object_or_404
from blog.models import Post,Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from blog.forms import Comment_form
from django.contrib import messages
# Create your views here.
def blog_view(request , **kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        posts = Post.objects.filter(category__name = kwargs['cat_name'])
    if kwargs.get('author_username') != None :
        posts = posts.filter(author__username = kwargs['author_username'])
    posts = Paginator(posts , 8)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = Paginator.page(1)
    except EmptyPage:
        posts = Paginator.page(1)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html' , context)
def blog_single(request , pid):
    if request.method == 'POST':
        form = Comment_form(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request , messages.SUCCESS , 'نظر شما با موفقیت ثبت شد .')
        else:
                messages.add_message(request , messages.ERROR, 'نظر شما ثبت نشد .دوباره تلاش کنید!')
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts , pk=pid , status =1)
    comments = Comment.objects.filter(post = post.id , approved=True)
    form = Comment_form()
    context = {'post':post , 'comments':comments , 'form':form}
    return render(request,'blog/blog-single.html' , context)

def blog_categories(request,cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html' , context)

def blog_search(request):
    posts = Post.objects.filter(status = 1)
    if request.method =='GET':
        posts = posts.filter(content__contains = request.GET.get('s'))
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html' , context)