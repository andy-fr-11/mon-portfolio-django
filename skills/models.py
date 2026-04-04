from django.db import models

class SkillCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom de la catégorie")
    icon = models.CharField(max_length=50, default='fas fa-code')
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order']
        verbose_name = "Catégorie de compétence"
        verbose_name_plural = "Catégories de compétences"

class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="Compétence")
    proficiency = models.IntegerField(help_text="Niveau de maîtrise (0-100)")
    years_experience = models.DecimalField(max_digits=3, decimal_places=1)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order']