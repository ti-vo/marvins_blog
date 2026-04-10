from django.shortcuts import render, get_object_or_404
from .models import Post



# Create your views here.

def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3] # Django behind the scenes only fetches 3 database entries. Does not support negative indexes
    #sorted_posts = sorted(all_posts, key=get_date)
    #latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts": latest_posts})

def posts(request):
    all_posts = Post.objects.all().order_by("-date") # -date descending order
    return render(request, "blog/all-posts.html", {
       "all_posts": all_posts
    }) 

def single_post(request, slug):

    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html",
                  {"post": identified_post,
                   "post_tags": identified_post.tags.all()})
