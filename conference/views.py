from django.shortcuts import render, redirect
from django.utils import translation
from django.conf import settings
from .models import ConferenceDay, SpeakerGroup, AboutPage, GalleryDay, GalleryHero
from .models import CustomsObject
from .models import SocialEvent

def set_language(request):
    lang = request.GET.get('lang', 'en')
    if lang in [l[0] for l in settings.LANGUAGES]:
        translation.activate(lang)
        request.session[translation.LANGUAGE_SESSION_KEY] = lang
    return redirect(request.META.get('HTTP_REFERER', '/'))


def index(request):
    return render(request, 'conference/index.html')


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
    objects = CustomsObject.objects.all()
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

