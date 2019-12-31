from django.contrib import admin

# Register your models here.

from .models import PostComment, PostImage, Post, PostLike


@admin.register(Post)
class PostAdmin(admin.decorators):
    pass


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    pass


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    pass

