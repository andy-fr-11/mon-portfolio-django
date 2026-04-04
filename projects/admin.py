from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'order', 'date_created']
    list_editable = ['featured', 'order']
    list_filter = ['featured', 'date_created']
    search_fields = ['title', 'technologies']
    prepopulated_fields = {}