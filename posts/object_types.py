import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth.models import User
from posts.models import Post

class UserType(DjangoObjectType):
    class Meta:
        model = User

class PostType(DjangoObjectType):
    author = graphene.Field(UserType)
    class Meta:
        model = Post