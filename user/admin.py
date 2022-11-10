from django.contrib import admin

from .models import  Post, Film, Staff


@admin.action(description='Опубликовать')
def make_published(self, request, queryset):
    queryset.update(is_published=True)


@admin.action(description='Снять с публикации')
def make_unpublished(self, request, queryset):
    queryset.update(is_published=False)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', 'subtitle')}
    list_display = ('title', 'author', 'date_published')
    date_hierarchy = 'date_published'
    list_filter = ('is_published', )
    readonly_fields = ('date_published', )
    actions = (make_published, make_unpublished)
    search_fields = ('title', 'id', 'subtitle')


@admin.register(Film)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('film_name',)
    list_filter = ('release_year', )
    search_fields = ('film_name', 'film_id')


@admin.register(Staff)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('staff_name',)
    list_filter = ('year_of_birth', )
    search_fields = ('staff_name', 'staff_id')
