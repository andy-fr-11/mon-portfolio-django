from django.shortcuts import render
from django.http import HttpResponse

def project_list(request):
    return HttpResponse("Liste des projets - En construction")

def project_detail(request, pk):
    return HttpResponse(f"Détail du projet {pk} - En construction")
