from modeltranslation.translator import register, TranslationOptions
from .models import CustomsObject
from .models import (
    ConferenceDay, AgendaSession,
    SpeakerGroup, Speaker,
    AboutPage, AboutSection, AboutBullet
)
from .models import SocialEvent


@register(ConferenceDay)
class ConferenceDayTranslation(TranslationOptions):
    fields = ('title', 'label', 'month')


@register(AgendaSession)
class AgendaSessionTranslation(TranslationOptions):
    fields = ('session_text', 'sub_items')


@register(SpeakerGroup)
class SpeakerGroupTranslation(TranslationOptions):
    fields = ('title',)


@register(Speaker)
class SpeakerTranslation(TranslationOptions):
    fields = ('name', 'title', 'organization', 'bio')


@register(AboutPage)
class AboutPageTranslation(TranslationOptions):
    fields = ('title', 'theme', 'date_location')


@register(AboutSection)
class AboutSectionTranslation(TranslationOptions):
    fields = ('heading', 'body', 'body_after')


@register(AboutBullet)
class AboutBulletTranslation(TranslationOptions):
    fields = ('text',)



@register(CustomsObject)
class CustomsObjectTranslation(TranslationOptions):
    fields = ('name', 'description')




@register(SocialEvent)
class SocialEventTranslation(TranslationOptions):
    fields = ('title', 'description', 'date', 'location')


from .models import GalleryDay, GalleryPhoto, GalleryHero

@register(GalleryHero)
class GalleryHeroTranslation(TranslationOptions):
    fields = ('title',)

@register(GalleryDay)
class GalleryDayTranslation(TranslationOptions):
    fields = ('title', 'date')

@register(GalleryPhoto)
class GalleryPhotoTranslation(TranslationOptions):
    fields = ('caption',)

from .models import Hotel, HotelRoom

@register(Hotel)
class HotelTranslation(TranslationOptions):
    fields = ('name', 'description', 'address', 'distance')

@register(HotelRoom)
class HotelRoomTranslation(TranslationOptions):
    fields = ('room_type', 'per')

from .models import Venue, VenueDay

@register(Venue)
class VenueTranslation(TranslationOptions):
    fields = ('name', 'subtitle', 'description')

@register(VenueDay)
class VenueDayTranslation(TranslationOptions):
    fields = ('day_label', 'date')


from .models import HomePage

@register(HomePage)
class HomePageTranslation(TranslationOptions):
    fields = ('title', 'subtitle', 'location', 'date', 'body_1', 'body_2', 'body_3', 'body_4')

from .models import ContactPerson

@register(ContactPerson)
class ContactPersonTranslation(TranslationOptions):
    fields = ('name', 'organization')