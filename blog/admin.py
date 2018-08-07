from django.contrib import admin
from blog.models import Post, Category


class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slugs': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slugs': ('title',)}


admin.site.register(Post)
admin.site.register(Category)


