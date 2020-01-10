from django.contrib.auth import authenticate, login, get_user_model, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignupForm
User = get_user_model()
# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('posts:post-list')
        else:
            return redirect('members:login')
    return render(request, 'members/login.html')


def signup_view(request):
    if request.method == "POST":


        if form.is_valid():
            email = request.POST['email']
            name = request.POST['name']
            username = request.POST['username']
            password = request.POST['password']
            
            form.save(email=email, name=name, username=username, password=password)
            user = User.objects.get(email=email)
            login(request, user)
            return redirect('posts:post-list')
        else:
            form = SignupForm()

        return render(request, 'members:login')
    # email = request.POST['email']
    # username = request.POST['username']
    # name = request.POST['name']
    # password = request.POST['password']
    #
    # if User.objects.filter(username=username).exists():
    #     return HttpResponse('이미 사용중인 username 입니다')
    # if User.objects.filter(email=email).exists():
    #     return HttpResponse('이미 사용중인 email입니다.')
    #
    # user = User.objects.create_user(
    #     password=password,
    #     username=username,
    #     email=email,
    #     name=name,
    #
    # )



def logout_view(request):
    logout(request)
    return redirect('members:log_in')