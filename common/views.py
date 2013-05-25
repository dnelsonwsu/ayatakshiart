from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404
from gallery.models import GalleryImage
from gallery.models import Medium
from gallery.models import Category

def index(request):
    return HttpResponse("Hello, world. You're the galleries index.")

def home(request):

    mediums_menu = Medium.objects.all()
    
    context = {'mediums_menu': mediums_menu,}
    
    return render(request, 'common/home.html', context)

    