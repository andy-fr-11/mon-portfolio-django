from core.models import Profile, Experience, Education, SocialLink
from skills.models import SkillCategory, Skill
from projects.models import Project
from datetime import date

profile, created = Profile.objects.get_or_create(
    name='Anderson Kontchou',
    defaults={
        'title': 'Technicien Supérieur en Systèmes et Réseaux',
        'bio': "Technicien Supérieur en Systèmes et Réseaux, spécialisé en administration réseau, sécurité et développement d'applications. Passionné par l'intelligence artificielle appliquée à la sécurité réseau et la création de solutions web professionnelles.",
        'email': 'andyfr11072002@gmail.com',
        'phone': '+237 6 55 41 01 29',
        'location': 'Yaoundé, Awae (Cameroun)',
        'nationality': 'Camerounais',
        'birth_date': date(2005, 4, 21),
        'marital_status': 'Célibataire',
    }
)
profile.nationality = 'Camerounais'
profile.birth_date = date(2005, 4, 21)
profile.marital_status = 'Célibataire'
profile.location = 'Yaoundé, Awae (Cameroun)'
profile.email = 'andyfr11072002@gmail.com'
profile.phone = '+237 6 55 41 01 29'
profile.title = 'Technicien Supérieur en Systèmes et Réseaux'
profile.bio = "Technicien Supérieur en Systèmes et Réseaux, spécialisé en administration réseau, sécurité et développement d'applications. Passionné par l'intelligence artificielle appliquée à la sécurité réseau et la création de solutions web professionnelles."
profile.save()

Experience.objects.all().delete()
Education.objects.all().delete()
SocialLink.objects.filter(name__in=['GitHub', 'LinkedIn']).delete()
Project.objects.filter(title__in=['Site de gestion Ontchop', 'Support JTK Multiservice']).delete()
SkillCategory.objects.filter(name__in=['Langages de programmation', 'Bases de données', 'Outils & environnements', 'Conception & modélisation', 'Gestion de projet']).delete()

Experience.objects.create(
    title='Informaticien polyvalent',
    company='OnTchop',
    location='Lomé, Togo',
    start_date=date(2023, 12, 1),
    current=True,
    description='Développement d’un site de gestion et de suivi du restaurant Ontchop, contributions en design graphique et optimisation des processus.',
    order=1,
)
Experience.objects.create(
    title='Secrétariat bureautique',
    company='JTK Multiservice',
    location='Yaoundé, Nkolanga',
    start_date=date(2024, 9, 1),
    current=True,
    description='Gestion des tâches de secrétariat, support administratif et coordination de services.',
    order=2,
)

Education.objects.create(
    degree='DTS en Systèmes et Réseaux',
    institution='IAI Cameroun',
    location='Yaoundé, Nkolanga',
    start_date=date(2024, 10, 1),
    end_date=date(2025, 10, 1),
    description='Projet : Intelligence Artificielle appliquée à la sécurité réseaux – Mention Très Bien (19/20).',
    order=1,
)
Education.objects.create(
    degree='Baccalauréat C',
    institution='Lycée Général Leclerc',
    location='Yaoundé',
    start_date=date(2021, 9, 1),
    end_date=date(2022, 5, 31),
    description='Orientation scientifique, spécialité mathématiques et physique.',
    order=2,
)

SocialLink.objects.create(name='GitHub', url='https://github.com/andersonkontchou', icon='fab fa-github', order=1)
SocialLink.objects.create(name='LinkedIn', url='https://linkedin.com/in/andersonkontchou', icon='fab fa-linkedin', order=2)

lang_cat = SkillCategory.objects.create(name='Langages de programmation', icon='fas fa-code', order=1)
Skill.objects.create(category=lang_cat, name='Python', proficiency=90, years_experience=3.0, order=1)
Skill.objects.create(category=lang_cat, name='Java', proficiency=70, years_experience=2.0, order=2)
Skill.objects.create(category=lang_cat, name='C++', proficiency=65, years_experience=1.5, order=3)
Skill.objects.create(category=lang_cat, name='PHP', proficiency=70, years_experience=2.0, order=4)
Skill.objects.create(category=lang_cat, name='JavaScript', proficiency=75, years_experience=2.0, order=5)

db_cat = SkillCategory.objects.create(name='Bases de données', icon='fas fa-database', order=2)
Skill.objects.create(category=db_cat, name='MySQL / PostgreSQL', proficiency=75, years_experience=2.0, order=1)
Skill.objects.create(category=db_cat, name='MongoDB', proficiency=70, years_experience=1.5, order=2)
Skill.objects.create(category=db_cat, name='SQLAlchemy / Sequelize', proficiency=70, years_experience=1.5, order=3)

tools_cat = SkillCategory.objects.create(name='Outils & environnements', icon='fas fa-tools', order=3)
Skill.objects.create(category=tools_cat, name='Visual Studio Code', proficiency=85, years_experience=3.0, order=1)
Skill.objects.create(category=tools_cat, name='Eclipse', proficiency=70, years_experience=2.0, order=2)
Skill.objects.create(category=tools_cat, name='GitHub / GitLab', proficiency=75, years_experience=2.0, order=3)

concept_cat = SkillCategory.objects.create(name='Conception & modélisation', icon='fas fa-project-diagram', order=4)
Skill.objects.create(category=concept_cat, name='Design orienté objet (OO)', proficiency=80, years_experience=2.5, order=1)
Skill.objects.create(category=concept_cat, name='Modélisation UML', proficiency=75, years_experience=2.0, order=2)
Skill.objects.create(category=concept_cat, name='Design patterns', proficiency=70, years_experience=2.0, order=3)

pm_cat = SkillCategory.objects.create(name='Gestion de projet', icon='fas fa-tasks', order=5)
Skill.objects.create(category=pm_cat, name='Agile / Scrum', proficiency=75, years_experience=1.5, order=1)

Project.objects.create(
    title='Site de gestion Ontchop',
    description='Développement en cours d’une plateforme de gestion et de suivi pour le restaurant Ontchop, avec un focus sur l’administration des commandes et le reporting.',
    technologies='Python, Django, HTML/CSS, JavaScript',
    project_url='https://github.com/andersonkontchou/ontchop',
    github_url='https://github.com/andersonkontchou/ontchop',
    date_created=date(2024, 12, 1),
    featured=True,
    order=1,
)
Project.objects.create(
    title='Support JTK Multiservice',
    description='Production de solutions de secrétariat bureautique et support administratif pour JTK Multiservice.',
    technologies='Office, PHP, gestion de documents',
    featured=False,
    date_created=date(2024, 9, 1),
    order=2,
)
print('CV data imported successfully!')
