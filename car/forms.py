from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from .models import Comment, CarModel
class CreateUser(UserCreationForm):
    first_name = forms.CharField(required=True)
    class Meta:
        model = User
        fields= ['username', 'first_name', 'email',]

class CommentFrom(forms.ModelForm):
    class Meta:
        model = Comment
        
        fields = ['nam','body']
class ChangeUserData(UserChangeForm):
    class Meta:
        model = User
        
        fields = ['username', 'first_name', 'email']