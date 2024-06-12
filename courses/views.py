from django.http import HttpResponse # type: ignore



def home(request):
    return HttpResponse("Home Page")