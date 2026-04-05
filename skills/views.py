from django.shortcuts import render
from .models import SkillCategory

def skill_list(request):
    skill_categories = SkillCategory.objects.prefetch_related('skills')
    return render(request, 'skills/list.html', {'skill_categories': skill_categories})
