from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="landing_page"),
    path("posts", views.AllPostsView.as_view(), name="posts_page"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post-detail-page")  # posts/my-first-post is search engine friendly
]