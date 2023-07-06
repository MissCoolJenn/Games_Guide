from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'game', 'title', 'body', 'img')

admin.site.register(Post, PostAdmin)