from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
import ayatakshiart.settings as settings
from gallery.models import Medium
from cart import Cart

def get_common_context(request):
    mediums_menu = Medium.objects.all()
    cart = Cart(request)
    context = {'mediums_menu': mediums_menu,
               'cart' : cart,
               'checkouturl': settings.PAYPAL_EMAIL,}
    return context


def home(request):
    context = get_common_context(request)
    return render_to_response('common/home.html', context, context_instance=RequestContext(request))


def thankyou(request):
    context = get_common_context(request)
    
    cart = Cart(request)
    cart.clear()   
    
    return render_to_response('common/thankyou.html', context, context_instance=RequestContext(request))

def index(request):
    context = get_common_context(request)
    
    cart = Cart(request)
    cart.clear()   
    
    return render_to_response('common/default.html', context, context_instance=RequestContext(request))