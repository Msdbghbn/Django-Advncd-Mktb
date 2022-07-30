from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


# getting user model object
User=get_user_model()


class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    content=models.TextField()
    status=models.BooleanField()
    category=models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    image=models.ImageField(null=True, blank=True)
    

    created_date=models.DateTimeField(auto_now_add=True)
    published_date=models.DateTimeField()
    updated_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name