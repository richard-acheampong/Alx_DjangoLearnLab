from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required= True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']  # Customize which fields you want to allow the user to edit    


# post form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # Fields for post creation and update

    def save(self, commit=True):
        # Automatically set the author to the current user when creating or updating a post
        post = super().save(commit=False)
        if commit:
            post.author = self.user  # Assuming you're passing the user during save
            post.save()
        return post
