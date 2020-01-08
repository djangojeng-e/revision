from django import forms
from django.forms import PasswordInput
from django.http import HttpResponse

from members.models import User


class LoginForm(forms.Form):
    # 로그인 시 사용
    pass


class SignupForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField()
    username = forms.CharField()
    password = forms.CharField(max_length=12, widget=PasswordInput,required=True)

    def save(self, email, name, username, password):
        if User.objects.filter(email=email):
            return HttpResponse('이미 존재하는 email입니다!')
        if User.objects.filter(username=username):
            return HttpResponse('이미 존재하는 username입니다.')
        else:
            return User.objects.create_user(
                email=self.cleaned_data['email'],
                name=self.cleaned_data['name'],
                username=self.cleaned_data['username'],
                password=self.cleaned_data['password'],
            )
