import graphene
from graphql import GraphQLError
from posts.forms import PostForm
from posts.models import Post
from django.contrib.auth.models import User


class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        sub_title = graphene.String(required=True)
        body = graphene.String(required=True)
        category_id = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, title, sub_title, body, category_id, **kwargs):
        user = info.context.user
        if not user.is_authenticated:
            raise GraphQLError("You must be logged in to create a post")

        form = PostForm(
            {
                "title": title,
                "sub_title": sub_title,
                "body": body,
                "category": category_id,
                "author": user,
            }
        )
        if form.is_valid():
            new_post = form.save()
            return CreatePost(success=True)
        print(form.errors)
        return CreatePost(success=False)


class UpdatePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String(required=True)
        sub_title = graphene.String(required=True)
        body = graphene.String(required=True)
        category_id = graphene.Int(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id, title, sub_title, body, category_id, **kwargs):
        user = info.context.user
        try:
            existing_post = Post.objects.get(id=id)
        except Post.DoesNotExist:
            raise GraphQLError("Post not found")

        # check if requesting user is the author of the post
        if existing_post.author != user:
            raise GraphQLError("You are not authorized to update this post")

        form = PostForm(
            {
                "title": title,
                "sub_title": sub_title,
                "body": body,
                "category": category_id,
                "author": user,
            },
            instance=existing_post,
        )
        if form.is_valid():
            updated_post = form.save()
            return UpdatePost(success=True)
        print(form.errors)
        return UpdatePost(success=False)


class DeletePost(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, id, **kwargs):
        user = info.context.user
        try:
            existing_post = Post.objects.get(id=id)
        except Post.DoesNotExist:
            raise GraphQLError("Post not found")
        
        if existing_post.author != user:
            raise GraphQLError("You are not authorized to delete this post")

        existing_post.delete()
        return DeletePost(success=True)
