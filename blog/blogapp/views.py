from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects #Queryset

    # Paginating
    # Get All Object
    blog_list = Blog.objects.all()
    # Split Object with Paginator
    paginator = Paginator(blog_list, 3)
    # Get Page with key 'page' which requested from user
    page = request.GET.get('page')
    # Notify page to paginator & Return
    posts = paginator.get_page(page)

    return render(request, 'home.html',{'blogs':blogs, 'posts':posts})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details':details})

def new(request):
    return render(request, 'new.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def create(request): #입력받은 내용을 DB에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() #Queryset Method로, 객체에 들어간 내용을 DB에 저장
    return redirect('/blog/'+str(blog.id))
