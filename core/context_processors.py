from .models import SocialLink

def site_info(request):
    return {
        'social_links': SocialLink.objects.all(),
    }