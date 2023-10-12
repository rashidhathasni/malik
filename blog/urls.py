from django.urls import path
from .import views
urlpatterns=[
    path("",views.index,name="index"),
    path("post",views.post,name="post"),
    path("display/<int:id>",views.display,name="display"),
    path("register",views.register,name="register")
]