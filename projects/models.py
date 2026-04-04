from django.db import models
from ckeditor.fields import RichTextField

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titre du projet")
    description = RichTextField(verbose_name="Description")
    technologies = models.CharField(max_length=300, verbose_name="Technologies utilisées")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    project_url = models.URLField(blank=True, verbose_name="Lien du projet")
    github_url = models.URLField(blank=True)
    date_created = models.DateField(verbose_name="Date de création")
    featured = models.BooleanField(default=False, verbose_name="Projet à la une")
    order = models.IntegerField(default=0, verbose_name="Ordre d'affichage")
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-featured', 'order', '-date_created']
        verbose_name = "Projet"
        verbose_name_plural = "Projets"