from django.db import models
from django.db import models
from categories.models import Category
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=120)
    sub_title = models.CharField(max_length=240)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Meta:
    permissions = [
        ("can_update_post", "Can update post"),
        ("can_delete_post", "Can delete post"),
    ]
