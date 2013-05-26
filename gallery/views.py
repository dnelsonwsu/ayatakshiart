from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404
from gallery.models import GalleryImage
from gallery.models import Medium
from gallery.models import Category
from gallery.models import PrintSize
from common.views import get_common_context

def index(request):
    return HttpResponse("Hello, world. You're the galleries index.")

def gallery(request, medium, category=None):

    if category == None:
        category = Category.objects.all()[0].name    #just use first category as default

    selected_images = get_list_or_404(GalleryImage, medium=medium, category=category)
    mediums_menu = Medium.objects.all()
    
    category_menu = []
    for i in GalleryImage.objects.filter(medium=medium):
        print "i.category: " + str(i.category)
        print "category: " + str(category)
        print "equal? " + str(i.category.name == category)

        if not i.category in category_menu and not i.category.name == category:
            print "ADD"
            category_menu.append(i.category)
    
    
    default_img = selected_images[0]
    
    print_sizes = PrintSize.objects.all()
    
    context = get_common_context(request)
        
    context['category_menu'] = category_menu 
    context['medium'] = medium
    context['category'] = category
    context['default_img'] = default_img
    context['selected_images'] = selected_images
    context['print_sizes'] = print_sizes
    
    return render(request, 'gallery/gallery.html', context)

    
    