from django.shortcuts import render
from .models import Blog

# Create your views here.
def blog(request):
    # Blog 테이블에 있는 객체들을 싹 다 가져와서 blogs에 저장
    blogs = Blog.objects.all()
    return render(request,'blog.html',{'blogs':blogs})