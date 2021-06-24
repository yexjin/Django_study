from django.shortcuts import render,get_object_or_404
from .models import Blog

# Create your views here.
def blog(request):
    # Blog 테이블에 있는 객체들을 싹 다 가져와서 blogs에 저장
    blogs = Blog.objects.all()
    return render(request,'blog.html',{'blogs':blogs})

def detail(request, id):
    blog = get_object_or_404(Blog,pk = id)
    return render(request, 'detail.html', {'blog':blog})