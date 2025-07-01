from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200) # Title of the blog post inside 200 characters
    content  = models.TextField() # Content of the blog post posses no limit
    created_at = models.DateTimeField(auto_now_add=True) # Automatically set the date and time when the post is created
    
    def __str__(self):
        return self.title  # Return the title of the post when the object is printed
    def get_absolute_url(self):
        return reverse("Post-detail", args=[str(self.id)])
    