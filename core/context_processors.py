from .models import Profile, SocialLink

def site_info(request):
    return {
        'social_links': SocialLink.objects.all(),
        'site_profile': Profile.objects.first(),
    }