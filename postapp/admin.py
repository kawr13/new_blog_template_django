from django.contrib import admin
from .models import Post, Comment, ImagesPost, Gallery_images
from django.utils.html import mark_safe
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
    ordering = ('-publish', 'status')
    inlines = [CommentTabularInline, ImagesPostTabularInline]


@admin.register(Gallery_images)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_image', 'created_at')
    list_filter = ('created_at',)
    list_related = ('created_at',)
    search_fields = ('title', 'image')
    ordering = ('-created_at',)

    def display_image(self, obj):
        # Здесь вы можете создать HTML-код для отображения изображения
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        else:
            return 'Нет изображения'

    display_image.short_description = 'Изображение'