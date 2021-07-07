from django.contrib import admin

# Register your models here.
from . import models

class CommentAdmin(admin.ModelAdmin):
    list_display = ['pk', 'comment_text', 'author', 'created', 'content_type', 'object_id']

admin.site.register(models.Comment, CommentAdmin)
