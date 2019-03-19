from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    """Model representing intracacies of a post"""
    title = models.CharField(max_length=200, null=True, blank=True)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    url = models.URLField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
    date_added = models.DateField('Date Added', auto_now_add=True, null=True, blank=True)
    slug = models.SlugField(unique=True)

    # Metadata
    class Meta: 
        ordering = ['-date_added']

    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])    

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)    

    def set_slug(self):
        # If the slug is already set, stop here.
        if self.slug:
            return

        base_slug = slugify(self.title)
        slug = base_slug
        n = 0

        # while we can find a record already in the DB with the slug
        # we're trying to use
        while Post.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + "-" + str(n)

        self.slug = slug       

class Comment(models.Model):
    user_comment = models.TextField(max_length=2000)

    def __str__(self):
        """String for representing the string representation of book object (in Admin site etc.)."""
        return self.user_comment


class Favorite(models.Model):        
    user_fav = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    favorited_at = models.DateTimeField(auto_now_add=True)
