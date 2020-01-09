from django import forms
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