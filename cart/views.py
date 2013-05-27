from django.http import HttpResponse, HttpResponseServerError
from django.utils import simplejson
from cart import Cart
from gallery.models import GalleryImage
from gallery.models import PrintSize

def cart_update(request):
    if request.method == "POST" and request.is_ajax:
        msg = "The operation has been received correctly."          
        print request.POST

        ##todo 404 if cant find
        img = GalleryImage.objects.get(name=request.POST['name'])
        print "aa"
        print str(img)
        
        printsize = PrintSize.objects.get(print_size=request.POST['size'])
        print printsize
        
        cart = Cart(request)
        cart.add(product=img, unit_price=printsize.price)
        
        data = {"cartcount": len(cart.items()) }
        
        json = simplejson.dumps(data)
        
        return HttpResponse(json, mimetype='application/json')
    else:
        return  HttpResponseServerError("GET petitions are not allowed for this view.")

    
