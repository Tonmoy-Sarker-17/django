from django.db import models
from catagories.models import Catagory
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your models here.

class Post(models.Model):
    tittle=models.CharField(max_length=50)
    content=models.TextField()
    catagory=models.ManyToManyField(Catagory) #ekta post multiple catagory te thkte pare ekta catagory te multiple post thkte pare
    author=models.ForeignKey(User, on_delete=models.CASCADE) #author delete hoile sob post o delete
    # author=models.ForeignKey(Author, on_delete=models.SET_NULL) #author delete hoile sob post thkbe
    image= models.ImageField(upload_to='uploads/',blank=True,null=True)
    # image= models.ImageField(upload_to='post/media/uploads/',blank=True,null=True)


    def __str__(self) -> str:
        return self.tittle
    
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=30)
    email=models.EmailField()
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True) #jkhn ei object create hobe time ta rekhe dibe

    def __str__(self) -> str:
        return f"comments by {self.name} "