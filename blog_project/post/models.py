from django.db import models
from catagories.models import Catagory
from author.models import Author

# Create your models here.

class Post(models.Model):
    tittle=models.CharField(max_length=50)
    content=models.TextField()
    catagory=models.ManyToManyField(Catagory) #ekta post multiple catagory te thkte pare ekta catagory te multiple post thkte pare
    author=models.ForeignKey(Author, on_delete=models.CASCADE) #author delete hoile sob post o delete
    # author=models.ForeignKey(Author, on_delete=models.SET_NULL) #author delete hoile sob post thkbe
    
    def __str__(self) -> str:
        return self.tittle