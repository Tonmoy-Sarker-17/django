from django.db import models

# Create your models here.

class Author(models.Model):
    name= models.CharField(max_length=100)
    bio = models.TextField()
    phone_no= models.CharField(max_length=15)
    
    def __str__(self) -> str:
        return self.name