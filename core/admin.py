from django.contrib import admin
from .models import Profile, SocialLink, Experience, Education

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'phone']
    fieldsets = (
        ('Informations personnelles', {
            'fields': ('name', 'title', 'bio', 'email', 'phone', 'location')
        }),
        ('Médias', {
            'fields': ('profile_image', 'cv_file')
        }),
        ('Réseaux sociaux', {
            'fields': ('github_url', 'linkedin_url')
        }),
    )

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'order']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'start_date', 'end_date', 'current']
    list_filter = ['current', 'company']
    ordering = ['-start_date']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'start_date', 'end_date', 'current']
    list_filter = ['current', 'institution']
    ordering = ['-start_date']