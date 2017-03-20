from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('posted',)

admin.site.register(Blog, BlogAdmin)
