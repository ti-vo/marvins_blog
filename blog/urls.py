from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="landing_page"),
    path("posts", views.posts, name="posts_page"),
    path("posts/<slug:slug>", views.single_post, name="post-detail-page")  # posts/my-first-post is search engine friendly
]