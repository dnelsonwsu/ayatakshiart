from django.http import HttpResponse, HttpResponseServerError
from django.utils import simplejson
from django.shortcuts import get_list_or_404
from django.template import RequestContext
from django.shortcuts import render_to_response

from common.views import get_common_context
from cart import Cart
from gallery.models import GalleryImage
from gallery.models import PrintSize

def view_cart(request):
    
    context = get_common_context(request)
    
    #cart_total= Cart(request).total_price
    
    return render_to_response('cart/viewcart.html', context, context_instance=RequestContext(request))

def thankyou(request):
    context = get_common_context(request)
    
    cart = Cart(request)
    cart.clear()   
    
    return render_to_response('cart/thankyou.html', context, context_instance=RequestContext(request))

def remove_item_from_cart(request):
    if request.method == "POST" and request.is_ajax:
        print request.POST

        ##todo 404 if cant find
        
        
        cart = Cart(request)
        item = cart.get_item_by_id(request.POST["id"])
        
        cart.remove(item.product)
        
        data = {"cartcount": len(cart.items()),
                "id": request.POST["id"] }
        
        json = simplejson.dumps(data)
        
        return HttpResponse(json, mimetype='application/json')
    else:
        return  HttpResponseServerError("GET petitions are not allowed for this view.")

    

def add_item_to_cart(request):
    if request.method == "POST" and request.is_ajax:
        print request.POST

        ##todo 404 if cant find
        img = GalleryImage.objects.get(name=request.POST['name'])
        #print str(img)
        
        printsize = PrintSize.objects.get(print_size=request.POST['size'])
        #print printsize
        
        cart = Cart(request)
        cart.add(product=img, unit_price=printsize.price, description= printsize.print_size + " Print", quantity=1)
        
        data = {"cartcount": len(cart.items()) }
        
        json = simplejson.dumps(data)
        
        return HttpResponse(json, mimetype='application/json')
    else:
        return  HttpResponseServerError("GET petitions are not allowed for this view.")

    
