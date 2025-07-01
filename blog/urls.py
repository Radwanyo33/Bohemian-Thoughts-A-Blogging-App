from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),# Home page of the blog app
    path("post/<int:pk>", views.post_details, name = "post-detail"), # View Post Details
    path("post/new/", views.PostCreateView.as_view(), name = "post-create"),
    path("post/<int:pk>/edit/",views.PostUpdateView.as_view(), name = "post-update"), #update post
    path("post/<int:pk>/delete/",views.PostDeleteView.as_view(), name = "post-delete"), #delete post
]

