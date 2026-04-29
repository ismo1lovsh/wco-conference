from django.urls import path
from . import views

app_name = 'conference'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('customs-committee/', views.customs_committee, name='customs_committee'),
    path('agenda/', views.agenda, name='agenda'),
    path('speakers/', views.speakers, name='speakers'),
    path('set-language/', views.set_language, name='set_language'),
    path('social-events/', views.social_events, name='social_events'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('hotels/', views.hotels, name='hotels'),
    path('venue/', views.venue, name='venue'),
    path('discover/', views.discover, name='discover'),
    path('gala-dinner/', views.gala_dinner, name='gala_dinner'),
    path('online-translation/', views.online_translation, name='online_translation'),
]