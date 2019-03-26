from django.contrib import admin
from core.models import Post, Comment, Favorite

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Favorite)
class Favorite(admin.ModelAdmin):
    pass
