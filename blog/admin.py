from pdb import post_mortem
from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

        # Set the fields of the model that we want to display on the admin object list page
        list_display = ('title', 'slug', 'author', 'publish', 'status')
        list_filter = ('status', 'created', 'publish', 'author')
        search_fields = ('title', 'body')
        
        prepopulated_fields = {"slug": ("title",)}
        """automatically generate the value for SlugField fields from the title."""

        raw_id_fields = ('author',)
        date_hierarchy = 'publish'
        ordering = ('status', 'publish')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
        list_display = ('name', 'email', 'post', 'created', 'active')
        list_filter = ('created', 'updated', 'active')
        search_fields = ('name', 'email', 'body')