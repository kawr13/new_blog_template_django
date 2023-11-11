from django.contrib import admin
from .models import Post, Comment, ImagesPost
# Register your models here.


class CommentTabularInline(admin.TabularInline):
    model = Comment
    extra = 0


class ImagesPostTabularInline(admin.TabularInline):
    model = ImagesPost
    extra = 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created_at', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('-publish',)
    inlines = [CommentTabularInline, ImagesPostTabularInline]
