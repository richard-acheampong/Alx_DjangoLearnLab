from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics
from .serializers import PostSerializer
from .models import Post
from .permissions import IsAuthor
from django.urls import reverse_lazy
from .forms import PostForm
from django.shortcuts import get_object_or_404

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
    
#PostListView for displaying all post
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

#PostDetailview to show individual blog posts.
class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

#PostCreateView to allow authenticated users to create new posts.
class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

#PostUpdateView to enable post authors to edit their posts.
# class PostUpdateView(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthor]

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, generics.UpdateAPIView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'  # Template for the form

    def test_func(self):
        """
        This method checks if the current user is the author of the post.
        Only the author can update the post.
        """
        post = self.get_object()
        return post.author == self.request.user

    def get_success_url(self):
        """
        After the post is updated, redirect the user to the post detail page.
        """
        return reverse_lazy('post-detail', kwargs={'pk': self.object.pk})


#PostDeleteView to enable post authors to delete their posts
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, generics.DestroyAPIView):
    # queryset = Post.objects.all()
    # serializer_class = PostSerializer
    # permission_classes = [IsAuthor]
    model = Post
    template_name = 'post_confirm_delete.html'  # Template for confirming deletion

    def test_func(self):
        """
        This method checks if the current user is the author of the post.
        Only the author can delete the post.
        """
        post = self.get_object()
        return post.author == self.request.user

    def get_success_url(self):
        """
        After the post is deleted, redirect the user to the post list page.
        """
        return reverse_lazy('post-list')

