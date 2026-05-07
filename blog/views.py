from django.shortcuts import render, get_object_or_404
from typing import List
from django.views.generic import ListView, DetailView
from .models import Post



# Create your views here.

# class-based view
class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts" # the name to be passed on to template

    def get_queryset(self):
        """overwrite internal function to limit to three posts"""
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

# function based view, obsolete:
def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3] # Django behind the scenes only fetches 3 database entries. Does not support negative indexes
    #sorted_posts = sorted(all_posts, key=get_date)
    #latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", 
                  {"posts": latest_posts} #pass posts to template
                  )



class AllPostsView(ListView):
    template_name = "blog/all-post.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

# function based view, obsolete
def posts(request):
    all_posts = Post.objects.all().order_by("-date") # -date descending order
    return render(request, "blog/all-posts.html", {
       "all_posts": all_posts
    }) 

# class based view
class SinglePostView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post
    # will automatically search by slug!

    def get_context_data(self, **kwargs):
        """overwrite to show tags""" 
        context_data = super().get_context_data(**kwargs)
        context_data["post_tags"] = self.object.tags.all()
        return context_data
       

# obsolete function based view:
def single_post(request, slug):

    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html",
                  {"post": identified_post,
                   "post_tags": identified_post.tags.all()})
