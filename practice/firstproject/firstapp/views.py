from django.shortcuts import render

def welcome(request):
    return render(request,"welcome.html")

def hello(request):
    userName = request.GET['name']
    # welcome.html에서 이름 가져오기
    return render(request,"hello.html", {'userName':userName})
    # hello.html로 userName이라는 이름을 가진 값이 들어가게 된다.
