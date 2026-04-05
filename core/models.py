from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom complet")
    title = models.CharField(max_length=200, verbose_name="Titre professionnel")
    bio = models.TextField(verbose_name="Biographie")
    email = models.EmailField()
    phone = models.CharField(max_length=20, verbose_name="Téléphone")
    location = models.CharField(max_length=200, verbose_name="Localisation")
    nationality = models.CharField(max_length=100, verbose_name="Nationalité", blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True, verbose_name="Date de naissance")
    marital_status = models.CharField(max_length=100, verbose_name="Situation familiale", blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    cv_file = models.FileField(upload_to='cv/', blank=True, null=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profils"

class Experience(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titre du poste")
    company = models.CharField(max_length=200, verbose_name="Entreprise")
    location = models.CharField(max_length=200, verbose_name="Lieu")
    start_date = models.DateField(verbose_name="Date de début")
    end_date = models.DateField(blank=True, null=True, verbose_name="Date de fin")
    description = models.TextField(verbose_name="Description")
    current = models.BooleanField(default=False, verbose_name="Poste actuel")
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.title} at {self.company}"
    
    class Meta:
        ordering = ['-start_date']
        verbose_name = "Expérience"
        verbose_name_plural = "Expériences"

class Education(models.Model):
    degree = models.CharField(max_length=200, verbose_name="Diplôme")
    institution = models.CharField(max_length=200, verbose_name="Établissement")
    location = models.CharField(max_length=200, verbose_name="Lieu")
    start_date = models.DateField(verbose_name="Date de début")
    end_date = models.DateField(blank=True, null=True, verbose_name="Date de fin")
    description = models.TextField(blank=True, verbose_name="Description")
    current = models.BooleanField(default=False, verbose_name="En cours")
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.degree} - {self.institution}"
    
    class Meta:
        ordering = ['-start_date']
        verbose_name = "Éducation"
        verbose_name_plural = "Éducations"

class SocialLink(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    icon = models.CharField(max_length=50, default='fab fa-github')
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order']