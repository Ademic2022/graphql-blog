from django.db import models
from django.db import models
from categories.models import Category


class Post(models.Model):
    title = models.CharField(max_length=120)
    sub_title = models.CharField(max_length=240)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
