from django.contrib import admin
from django.urls import path
from blog.views import * 
from blog import views as blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.blog, name="blog"),
    path('<str:id>', detail, name="detail"),
    path('new/',new,name="new"),
    path('create/',create, name="create"),
    path('edit/<str:id>', edit, name="edit"),
    path('update/<str:id>', update, name="update"),
    ## delete!!
    path('delete/<str:id>', delete, name="delete"),
]
