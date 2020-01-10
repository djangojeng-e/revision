from django.http import HttpResponse
from django.shortcuts import render, redirect

from members.forms import SignupForm


def index(request):
    if request.method == "POST":
        form = SignupForm(data=request.POST)

    if request.user.is_authenticated:
        return redirect('posts:post-list')
    return render(request, 'index.html', {'form': form})