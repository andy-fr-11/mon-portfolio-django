from django.shortcuts import render
from .models import Profile, Experience, Education
from skills.models import SkillCategory
from projects.models import Project

def home(request):
    profile = Profile.objects.first()
    experiences = Experience.objects.all()[:3]  # Limit to 3
    educations = Education.objects.all()[:2]  # Limit to 2
    skill_categories = SkillCategory.objects.prefetch_related('skills')
    featured_projects = Project.objects.filter(featured=True)[:3]
    context = {
        'profile': profile,
        'experiences': experiences,
        'educations': educations,
        'skill_categories': skill_categories,
        'featured_projects': featured_projects,
    }
    return render(request, 'core/home.html', context)
