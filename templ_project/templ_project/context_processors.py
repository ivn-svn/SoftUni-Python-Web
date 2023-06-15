from django.urls import reverse

def navigation_links(request):
    contact_url = reverse('contact_page')
    gallery_url = reverse('gallery_page')
    about_url = reverse('about_page')
    return {
        'contact_url': contact_url,
        'gallery_url': gallery_url,
        'about_url': about_url,
    }
