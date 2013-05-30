from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from gallery.models import Medium
from cart import Cart

def index(request):
    return HttpResponse("Hello, world. You're the galleries index.")

def get_common_context(request):
    mediums_menu = Medium.objects.all()
    cart = Cart(request)
    context = {'mediums_menu': mediums_menu,
               'cart' : cart,}
    return context


def home(request):
    context = get_common_context(request)
    return render_to_response('common/home.html', context, context_instance=RequestContext(request))

    