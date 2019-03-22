from django.contrib import admin
from core.models import Post, Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    