from django.shortcuts import render, redirect
from django.utils import translation
from django.conf import settings
from .models import ConferenceDay, SpeakerGroup, AboutPage, GalleryDay, GalleryHero
from .models import CustomsObject
from .models import SocialEvent

from django.utils import translation
from django.conf import settings


def set_language(request):
    lang = request.GET.get('lang', 'en')
    if lang not in [l[0] for l in settings.LANGUAGES]:
        lang = 'en'

    from django.utils.translation import activate
    activate(lang)
    request.session['_language'] = lang
    request.session.modified = True

    response = redirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie(
        'django_language',
        lang,
        max_age=365 * 24 * 60 * 60,
        path='/',
    )
    return response
from django.utils.translation import get_language

from .models import HomePage

def index(request):
    from django.utils.translation import get_language
    current_lang = request.session.get('_language', 'en')
    home = HomePage.objects.first()
    return render(request, 'conference/index.html', {
        'current_lang': current_lang,
        'home': home,
    })


def about(request):
    page = AboutPage.objects.prefetch_related('sections__bullets').first()
    return render(request, 'conference/about.html', {'page': page})


def agenda(request):
    days = ConferenceDay.objects.prefetch_related('sessions').all()
    return render(request, 'conference/agenda.html', {'days': days})


def speakers(request):
    groups = SpeakerGroup.objects.prefetch_related('speakers').all()
    return render(request, 'conference/speakers.html', {'groups': groups})


def customs_committee(request):
    return render(request, 'conference/customs_committee.html')


def customs_committee(request):
    objects = CustomsObject.objects.prefetch_related('images').all()
    return render(request, 'conference/customs_committee.html', {'objects': objects})



def social_events(request):
    events = SocialEvent.objects.all()
    return render(request, 'conference/social_events.html', {'events': events})




def gallery(request):
    days = GalleryDay.objects.prefetch_related('photos').all()
    hero = GalleryHero.objects.first()
    return render(request, 'conference/gallery.html', {
        'days': days,
        'hero': hero,
    })


from .models import ContactPerson

def contact(request):
    wco_contacts = ContactPerson.objects.filter(category='wco')
    registration = ContactPerson.objects.filter(category='registration')
    host_contacts = ContactPerson.objects.filter(category='host')
    return render(request, 'conference/contact.html', {
        'wco_contacts': wco_contacts,
        'registration': registration,
        'host_contacts': host_contacts,
    })


from .models import Hotel

def hotels(request):
    hotels = Hotel.objects.prefetch_related('rooms', 'images').all()
    return render(request, 'conference/hotels.html', {'hotels': hotels})


from .models import Venue

def venue(request):
    venues = Venue.objects.prefetch_related('days').all()
    return render(request, 'conference/venue.html', {'venues': venues})

from .models import DiscoverCity, DiscoverGalleryPhoto

def discover(request):
    current_lang = request.session.get('_language', 'en')
    cities = DiscoverCity.objects.prefetch_related('images', 'videos').all()
    gallery = DiscoverGalleryPhoto.objects.all()
    return render(request, 'conference/discover.html', {
        'cities': cities,
        'gallery': gallery,
        'current_lang': current_lang,
    })

from .models import GalaDinner

def gala_dinner(request):
    gala = GalaDinner.objects.prefetch_related('highlights').first()
    return render(request, 'conference/gala_dinner.html', {'gala': gala})

from .models import OnlineTranslation

def online_translation(request):
    translation_obj = OnlineTranslation.objects.first()
    return render(request, 'conference/online_translation.html', {
        'translation': translation_obj
    })

