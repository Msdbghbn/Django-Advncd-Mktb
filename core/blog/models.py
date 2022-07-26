from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# from accounts.models import Profile
# Create your models here.


# getting user model object
User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True
    )
    image = models.ImageField(null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField()
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_snippet(self):
        return self.content[0:5]

    def get_absolute_api_url(self):
        return reverse("blog:api-v1:post-detail", kwargs={"pk": self.pk})


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
