from django.shortcuts import render, get_object_or_404, redirect
from core.models import Post, Favorite
from django.views import generic
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
from core.forms import CommentForm

def index(request):
    """View function for the homepage of the site."""
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def sort_by_favorite(request):
    sort_by_favorite_posts = Post.objects.annotate(num_favorites=Count('favorite')).order_by('-num_favorites')
    return render(request, 'index.html', {'posts': sort_by_favorite_posts})

def sort_by_date_added(request):
    sort_by_date_added = Post.objects.order_by('-date_added')
    return render(request, 'index.html', {'posts': sort_by_date_added})

def post_detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "core/post_detail.html", {'post': post})

@require_http_methods(['POST'])
@login_required
def post_favorite_view(request, slug):
    post = get_object_or_404(Post, slug=slug)

    favorite, created = request.user.favorite_set.get_or_create(post=post)

    if created:
        messages.info(request, f"You have favorited {post.title}.")
    else:
        messages.info(request, f"You have unfavorited {post.title}.")
        favorite.delete()

    return redirect('index')

@login_required
def comment(request, slug):

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = Post.objects.get(slug=slug)
            comment.save()
            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm()
    return render(request, 'comment_new.html', {'form':form})
    # try core/comment (before moving file up dir)
    # got rid of .html after post_detail
