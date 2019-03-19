from django.shortcuts import render
from core.models import Post
from django.views import generic

def index(request):
    """View function for the homepage of the site."""

    posts = Post.objects.all()

    context = {
        'posts': posts,
    }    

    return render(request, 'core/index.html', context=context)

def post_detail_view(request, slug):
    posts = get_object_or_404(Event, slug=slug)
    return render(request, "core/post_detail.html", {"posts": posts})
