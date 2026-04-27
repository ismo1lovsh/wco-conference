from django.db import models


class ConferenceDay(models.Model):
    date = models.DateField()
    label = models.CharField(max_length=20)  # "7th", "8th", "9th"
    month = models.CharField(max_length=10)  # "SEP"
    title = models.CharField(max_length=200) # "Sunday, 7 September 2026"
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class AgendaSession(models.Model):
    STYLE_CHOICES = [
        ('normal', 'Normal'),
        ('break_1', 'Break 1'),
        ('break_2', 'Break 2'),
        ('break_3', 'Break 3'),
    ]

    day = models.ForeignKey(ConferenceDay, on_delete=models.CASCADE, related_name='sessions')
    time_start = models.CharField(max_length=10, blank=True)  # "09:00"
    time_end = models.CharField(max_length=10, blank=True)    # "10:30"
    session_text = models.TextField()
    sub_items = models.TextField(blank=True, help_text="Har bir qator yangi li bo'ladi")
    style = models.CharField(max_length=20, choices=STYLE_CHOICES, default='normal')
    rowspan = models.PositiveSmallIntegerField(default=1)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def get_sub_items(self):
        if self.sub_items:
            return [line.strip() for line in self.sub_items.splitlines() if line.strip()]
        return []

    def __str__(self):
        return f"{self.day} | {self.time_start} - {self.session_text[:50]}"


class SpeakerGroup(models.Model):
    title = models.CharField(max_length=200)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Speaker(models.Model):
    group = models.ForeignKey(SpeakerGroup, on_delete=models.CASCADE, related_name='speakers')
    name = models.CharField(max_length=300)
    title = models.CharField(max_length=300, blank=True)
    organization = models.CharField(max_length=300, blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='speakers/', blank=True, null=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class AboutPage(models.Model):
    title = models.CharField(max_length=300)
    theme = models.CharField(max_length=300)
    date_location = models.CharField(max_length=300)

    class Meta:
        verbose_name = "About Page"

    def __str__(self):
        return self.title


class AboutSection(models.Model):
    page = models.ForeignKey(AboutPage, on_delete=models.CASCADE, related_name='sections')
    heading = models.CharField(max_length=200, blank=True)
    body = models.TextField(blank=True)
    body_after = models.TextField(blank=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.heading


class AboutBullet(models.Model):
    section = models.ForeignKey(AboutSection, on_delete=models.CASCADE, related_name='bullets')
    text = models.TextField()
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.text[:60]



class CustomsObject(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='customs_objects/')
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class CustomsObjectImage(models.Model):
    obj = models.ForeignKey(CustomsObject, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='customs_objects/gallery/')
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.obj.name} - {self.order}"

class SocialEvent(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='social_events/')
    date = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=200, blank=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class GalleryHero(models.Model):
    image = models.ImageField(upload_to='gallery/hero/')
    title = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = "Gallery Hero Image"

    def __str__(self):
        return self.title or "Hero Image"


class GalleryDay(models.Model):
    title = models.CharField(max_length=100)
    date = models.CharField(max_length=100, blank=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class GalleryPhoto(models.Model):
    day = models.ForeignKey(GalleryDay, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='gallery/photos/')
    caption = models.CharField(max_length=300, blank=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.day.title} - {self.order}"


class ContactPerson(models.Model):
    CATEGORY_CHOICES = [
        ('wco', 'WCO Staff Contacts'),
        ('registration', 'Registration'),
        ('host', 'Host Country Focal Point'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=200)
    organization = models.CharField(max_length=300, blank=True)
    emails = models.TextField(help_text="Har bir email yangi qatorda")
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def get_emails(self):
        return [e.strip() for e in self.emails.splitlines() if e.strip()]

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=300, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    image = models.ImageField(upload_to='hotels/', blank=True, null=True)
    stars = models.PositiveSmallIntegerField(default=5)
    distance = models.CharField(max_length=100, blank=True)  # "500m to venue"
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class HotelRoom(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    room_type = models.CharField(max_length=200)  # "Single Room", "Double Room"
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default='USD')
    per = models.CharField(max_length=50, default='per night')
    breakfast_included = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.hotel.name} - {self.room_type}"

class Venue(models.Model):
    name = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='venues/', blank=True, null=True)
    google_maps_url = models.URLField(blank=True)
    google_maps_embed = models.TextField(blank=True, help_text="Google Maps iframe embed kodi")
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class VenueDay(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='days')
    day_label = models.CharField(max_length=100)  # "Opening Day", "Day 1"
    date = models.CharField(max_length=100, blank=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.venue.name} - {self.day_label}"


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='hotels/gallery/')
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.hotel.name} - {self.order}"


class HomePage(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=300, blank=True)
    location = models.CharField(max_length=200, blank=True)
    date = models.CharField(max_length=200, blank=True)
    body_1 = models.TextField(blank=True)
    body_2 = models.TextField(blank=True)
    body_3 = models.TextField(blank=True)
    body_4 = models.TextField(blank=True)
    illustration = models.ImageField(upload_to='home/', blank=True, null=True)
    youtube_id = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "Home Page"

    def __str__(self):
        return self.title