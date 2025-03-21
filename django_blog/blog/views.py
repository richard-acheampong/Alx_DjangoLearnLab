from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class Homeview(View):
        def get(self, request):
        # You can pass context variables to the template here if needed
            return render(request, 'home.html')

class RegisterView(View):
    def dispatch(self, request, *args, **kwargs):
        #check for method explicitly
        if request.nethod == 'POST':
            return self.method_post(request, *args, **kwargs )
        return self.method_get(request, *args, **kwargs)
    
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'registration/register.html', {'form' : form})
    
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'registration/register.html', {'form':form})
    
class ProfileView(View):
    @login_required
    def method_get(self, request):
        # Get the currently authenticated user
        user = request.user
        form = CustomUserChangeForm(instance=user)
        return render(request, 'profile.html', {'form': form})
        
    
    @login_required
    def method_post(self, request):
        # Handle form submission to update user profile
        # user = request.user
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, 'profile.html', {'form':form})