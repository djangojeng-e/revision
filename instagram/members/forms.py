from django import forms
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from django.forms import PasswordInput
from django.http import HttpResponse

from members.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '아이디'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호',
            }
        )
    )

    def clean(self):
        # Form.clean에서는 cleaned_data에 접근 가능
        # cleaned_data 에는
        # 이 Form 이 가진 모든 Field 들에서 리턴된 데이터가 key: value로 들어있음
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if not user:
            raise ValidationError('username또는 password가 올바르지 않습니다.')
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        login(request, user)


class SignupForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField()
    username = forms.CharField()
    password = forms.CharField(max_length=12, widget=PasswordInput, required=True)

    def save(self, email, name, username, password):
        """
        Form 으로 전달받은 데이터를 사용 해서
        새로운 User를 생성하고 리턴

        Username과 email 검증로직도 이 안에 넣기
        :param email:
        :param name:
        :param username:
        :param password:
        :return:
        """