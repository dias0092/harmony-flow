from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class UserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'date_of_birth', 'profile_image',)

class UserEditForm(UserChangeForm):
    password = None 

    class Meta:
        model = User
        fields = ['username', 'email', 'date_of_birth', 'profile_image']