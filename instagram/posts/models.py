from django.db import models

# Create your models here.
from members.models import User

class Post(models.Model):
    """
    인스타그램 포스트
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    like_users = models.ManyToManyField(
        User, through='PostLike', related_name='like_post_set',
    )
    created = models.DateTimeField(auto_now_add=True)



class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/images')


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()


class PostLike(models.Model):
    """
    사용자가 좋아요 누른 post정보를 저장
    Many-To-Many 필드를 중간모델 (Intermediate Model)을 거쳐 사용
    언제 생성 되었는지를 extra field에 저장! (created)
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
