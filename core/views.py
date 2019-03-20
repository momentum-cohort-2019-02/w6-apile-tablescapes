from django.shortcuts import render, get_object_or_404, redirect
from core.models import Post, Favorite
from django.views import generic

def index(request):
    """View function for the homepage of the site."""
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }    

    return render(request, 'index.html', context=context)

def post_detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "core/post_detail.html", {'post': post})

def post_fav_view(request, slug):
    post = get_object_or_404(Post, slug=slug)

    fav, created = request.favorite.favorite_fav_set.get_or_create(fav=fav)

    return redirect(index())

