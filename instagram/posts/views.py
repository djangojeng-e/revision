from django.shortcuts import render, redirect

# Create your views here.
from .models import Post, PostLike
from .forms import PostCreateForm, CommentCreateForm


def post_list(request):
    posts = Post.objects.order_by('-pk')
    comment_form = CommentCreateForm()
    context = {
        'posts': posts,
        'comment_form': comment_form
    }
    return render(request, 'posts/post-list.html', context)


def post_like(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user

    post_like_qs = PostLike.objects.filter(post=post, user=user)
    # user, post에 해당하는 PostLike가 있는 경우
    if post_like_qs.exists():
        post_like_qs.delete()
    else:
        PostLike.objects.create(post=post, user=user)

    return redirect('posts:post-list')


def post_create(request):

    if request.method == 'POST':
        text = request.POST['text']
        images = request.FILES.getlist('image')

        post = Post.objects.create(
            author=request.user,
            content=text
        )

        for image in images:
            post.postimage_set.create(image=image)

        return redirect('posts:post-list')
    else:
        form = PostCreateForm()
        context = {
            'form': form,
        }
        return render(request, 'posts/post-create.html', context)


def comment_create(request, post_pk):
    if request.method == "POST":
        post = Post.objects.get(pk=post_pk)
        # content = request.POST['content']
        #
        # post.postcomment_set.create(
        #     author=request.user,
        #     content=content,
        # )
        form = CommentCreateForm(data=request.POST)
        if form.is_valid():
            form.save(post=post, author=request.user)

        return redirect('posts:post-list')