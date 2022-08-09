from django.contrib import admin
from .models import Post, Category

# Register your models here.
admin.site.register(Category)
admin.site.register(Post)


class PostAdmin(admin.ModelAdmin):
    list_display = [
        "author",
        "title",
        "status",
        "category",
        "created_date",
        "published_date",
    ]
