from django.http import HttpResponse
from django.shortcuts import render
from gallery.models import Medium

def index(request):
    return HttpResponse("Hello, world. You're the galleries index.")

def get_common_context():
    mediums_menu = Medium.objects.all()
    context = {'mediums_menu': mediums_menu,}
    return context


def home(request):
    context = get_common_context()
    return render(request, 'common/home.html', context)

    