from django.contrib import admin
from django.urls import path
# views로 겹칠 경우 에러가 발생해서 as로 각각 이름지어주기
# from firstapp import views as first
# from wordCount import views as wc
from blog.views import * # 모든함수를 가져오겠다.
from blog import views as blog

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('welcome', first.welcome, name="welcome"),
    # name이라는 세번째 인수는 다른 html에서 url대신에 쉽게 사용할 수 있는 이름이다.
    # path('hello', first.hello, name="hello"),
    # path('wc/', wc.home, name="wc"),
    # path('wc/result/', wc.result, name="result"),
    path('', blog.blog, name="blog"),
    path('<str:id>', detail, name="detail"),
]
