from django.shortcuts import render, get_object_or_404, redirect
from core.models import Post, Favorite
from django.views import generic
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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

@require_http_methods(['POST'])
@login_required
def post_fav_view(request, slug):
    post = get_object_or_404(Post, slug=slug)

    favorite, created = request.user.favorite_set.get_or_create(post=post)

    if created:
        messages.info(request, f"You have favorited {post.title}.")
    else:
        messages.info(request, f"You have unfavorited {post.title}.")
        favorite.delete()

    return redirect('/core/')
