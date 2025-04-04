from .models import SocialLink

def social_links_processor(request):
    return {
        'social_links': SocialLink.objects.all()
    }
