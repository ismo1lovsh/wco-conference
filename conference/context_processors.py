from conference.models import HomePage

def home_data(request):
    try:
        home = HomePage.objects.first()
    except:
        home = None
    return {'home_data': home}