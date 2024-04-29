from django.contrib import admin
from . import models
from .models import Feedback

# Register your models here.

class NotesAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(models.Notes, NotesAdmin)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    search_fields = ['name', 'email', 'message']