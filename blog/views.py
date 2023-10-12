from django.shortcuts import render,redirect
from.forms import MakePost
from . models import Post 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def index(request):
    post=Post.objects.all()
    return render(request,"index.html",{'post':post})
@login_required
def post(request):
    form = MakePost()
    if request.method =='POST':
        form = MakePost(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'post.html',{'form':form})
def display(request,id):
    post=Post.objects.get(id=id)
    return render(request,'display.html',{'post':post})
def register(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,"register.html",{'form':form})
