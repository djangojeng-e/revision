from django.contrib.auth import authenticate, login, get_user_model, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
User = get_user_model()
# Create your views here.


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.login(request)
            return redirect('posts:post-list')

    else:
        form = LoginForm()

    context = {
        'form': form,
    }

    return render(request, 'members/login.html', context)


def signup_view(request):
    '''
    Template : index.html 을 그대로 사용
    action만 이쪽으로
    URL : /members/signup/
    FORM : members.forms.SignupForm

    User에 name필드를 추가
    email
    username
    name
    password
    를 전달받아, 새로운 User를 생성한다.
    생성시 User.objects.create.user() 메서드를 사용한다.

    이미 존재하는 username 또는 email을 입력한 경우,
    "이미 사용중인 username/email입니다" 라는 메시지를 HttpResponse로 돌려준다

    생성에 성공하면 로그인 처리 후 위의 (login_view를 참조) posts:post-list로 redirect 처리
    :param request:
    :return:
    '''
    email = request.POST['email']
    username = request.POST['username']
    name = request.POST['name']
    password = request.POST['password']

    if User.objects.filter(username=username).exists():
        return HttpResponse('이미 사용중인 username입니다')
    if User.objects.filter(email=email).exists():
        return HttpResponse('이미 사용중인 email입니다')

    user = User.objects.create_user(
        password=password,
        username=username,
        email=email,
        name=name,
    )
    login(request, user)
    return redirect('posts:post-list')


def logout_view(request):
    logout(request)
    return redirect('members:log_in')