from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .models import SocialEvent, HotelImage, CustomsObjectImage, HomePage, VenueImage
from .models import (
    ConferenceDay, AgendaSession,
    SpeakerGroup, Speaker,
    AboutPage, AboutSection, AboutBullet, CustomsObject
)
from .models import GalleryDay, GalleryPhoto


class AgendaSessionInline(admin.TabularInline):
    model = AgendaSession
    extra = 1
    fields = ('order', 'time_start', 'time_end', 'session_text', 'sub_items', 'style', 'rowspan')


@admin.register(ConferenceDay)
class ConferenceDayAdmin(admin.ModelAdmin):
    list_display = ('title', 'label', 'month', 'order')
    inlines = [AgendaSessionInline]


class SpeakerInline(TranslationTabularInline):
    model = Speaker
    extra = 1
    fields = ('order', 'name', 'title', 'organization', 'bio', 'photo')


@admin.register(SpeakerGroup)
class SpeakerGroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    inlines = [SpeakerInline]


class AboutSectionInline(admin.StackedInline):
    model = AboutSection
    extra = 1


class AboutBulletInline(admin.TabularInline):
    model = AboutBullet
    extra = 1


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    inlines = [AboutSectionInline]


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    inlines = [AboutBulletInline]


@admin.register(SocialEvent)
class SocialEventAdmin(TranslationAdmin):
    list_display = ('title', 'date', 'order')

from .models import GalleryHero, GalleryDay, GalleryPhoto

@admin.register(GalleryHero)
class GalleryHeroAdmin(TranslationAdmin):
    list_display = ('title',)

class GalleryPhotoInline(admin.TabularInline):
    model = GalleryPhoto
    extra = 5
    fields = ('order', 'image', 'caption')

@admin.register(GalleryDay)
class GalleryDayAdmin(TranslationAdmin):
    list_display = ('title', 'date', 'order')
    inlines = [GalleryPhotoInline]


from .models import ContactPerson


from .models import Hotel, HotelRoom
class HotelRoomInline(admin.TabularInline):
    model = HotelRoom
    extra = 3
    fields = ('order', 'room_type', 'price', 'currency', 'per', 'breakfast_included')

class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 3
    fields = ('order', 'image')

@admin.register(Hotel)
class HotelAdmin(TranslationAdmin):
    list_display = ('name', 'stars', 'order')
    inlines = [HotelRoomInline, HotelImageInline]

from .models import Venue, VenueDay

class VenueDayInline(admin.TabularInline):
    model = VenueDay
    extra = 1
    fields = ('order', 'day_label', 'date')

class VenueImageInline(admin.TabularInline):
    model = VenueImage
    extra = 3
    fields = ('order', 'image')

class VenueDayInline(admin.TabularInline):
    model = VenueDay
    extra = 1

@admin.register(Venue)
class VenueAdmin(TranslationAdmin):
    list_display = ('name', 'order')
    inlines = [VenueDayInline, VenueImageInline]


class CustomsObjectImageInline(admin.TabularInline):
    model = CustomsObjectImage
    extra = 3
    fields = ('order', 'image')

# CustomsObjectAdmin ni yangilang:
@admin.register(CustomsObject)
class CustomsObjectAdmin(TranslationAdmin):
    list_display = ('name', 'order')
    inlines = [CustomsObjectImageInline]

@admin.register(HomePage)
class HomePageAdmin(TranslationAdmin):
    list_display = ('title',)


@admin.register(ContactPerson)
class ContactPersonAdmin(TranslationAdmin):
    list_display = ('name', 'category', 'order')
    list_filter = ('category',)

from .models import DiscoverCity, DiscoverCityImage, DiscoverCityVideo, DiscoverGalleryPhoto

class DiscoverCityImageInline(admin.TabularInline):
    model = DiscoverCityImage
    extra = 3
    fields = ('order', 'image', 'caption')

class DiscoverCityVideoInline(admin.TabularInline):
    model = DiscoverCityVideo
    extra = 1
    fields = ('order', 'video_file', 'title')

@admin.register(DiscoverCity)
class DiscoverCityAdmin(TranslationAdmin):
    list_display = ('name', 'order')
    inlines = [DiscoverCityImageInline, DiscoverCityVideoInline]

@admin.register(DiscoverGalleryPhoto)
class DiscoverGalleryPhotoAdmin(admin.ModelAdmin):
    list_display = ('caption', 'order')

from .models import GalaDinner, GalaDinnerHighlight

class GalaDinnerHighlightInline(admin.TabularInline):
    model = GalaDinnerHighlight
    extra = 3

@admin.register(GalaDinner)
class GalaDinnerAdmin(TranslationAdmin):
    list_display = ('title',)
    inlines = [GalaDinnerHighlightInline]

from .models import OnlineTranslation

@admin.register(OnlineTranslation)
class OnlineTranslationAdmin(TranslationAdmin):
    list_display = ('is_live', 'stream_url')



