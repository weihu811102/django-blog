from django.contrib import admin
from models import Blog, Category

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "timestamp")
    list_filter = ("timestamp",)
    search_fields = ("title", "content")
    ordering = ("-timestamp", "title")
    #fields = ("title", "content", "category", "timestamp")


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
