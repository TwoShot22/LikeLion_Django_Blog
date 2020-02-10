from django import forms
from .models import Blog

class BlogPost(forms.ModelForm): #임의의 입력 공간 - forms.Form
    class Meta:
        model = Blog
        fields = ['title', 'body']