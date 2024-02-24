from django.shortcuts import render
from post.models import Post
from catagories.models import Catagory

def  home(request,category_slug=None):
    data=Post.objects.all()
    if category_slug is not None:
        category=Catagory.objects.get(slug=category_slug)
        data=Post.objects.filter(catagory=category)
        #category folder re catagory likhsi tai 
    categories=Catagory.objects.all()
    # print(data)
    return render(request,'home.html',{'data':data, 'category':categories})