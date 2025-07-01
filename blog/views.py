from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    posts = Post.objects.all() # Fetch all posts from the database
    return render(request, 'blog//home.html',{"posts":posts}) # Render the home template with the posts context

#View Post_Details
@login_required # Ensure that only logged-in users can view post details
def post_details(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request, 'blog/post_details.html', {"post":post}) # Render the post details template with the post context

#New Post
class PostCreateView(CreateView):
    model = Post
    template_name = "blog/post-form.html" # Template for creating a new post
    fields = ["title","content"] # Fields to be displayed in the form
    success_url = reverse_lazy("home") # Redirect to home after successful creation
#Update Post
class PostUpdateView(UpdateView):
    model = Post 
    template_name = "blog/post-edit.html" # Template for updating a post
    fields = ["title","content"] # Fields to be displayed in the form
    success_url = reverse_lazy("home")
#Delete Post
class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post-delete.html" # Template for deleting a post
    success_url = reverse_lazy("home") # Redirect to home after successful deletion
    
