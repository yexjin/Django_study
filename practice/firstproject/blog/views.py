from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Blog
from .forms import BlogForm
def blog(request):
    blogs = Blog.objects.all()
    return render(request,'blog.html',{'blogs':blogs})

def detail(request, id):
    blog = get_object_or_404(Blog,pk = id)
    return render(request, 'detail.html', {'blog':blog})

def new(request):
    form = BlogForm()
    return render(request, 'new.html')

def create(request):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():   #유효성 검사
        new_blog = form.save(commit=False) #임시 저장
        new_blog.pub_date = timezone.now()
        new_blog.save()
        return redirect('detail', new_blog.id)
    return redirect('blog')

def edit(request, id):
    edit_blog = Blog.objects.get(id= id)
    return render(request, 'edit.html', {'blog':edit_blog})

def update(request, id):
    update_blog = Blog.objects.get(id= id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now( )    
    update_blog.save() 
    return redirect('detail', update_blog.id)

# DELETE !!
def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('blog')