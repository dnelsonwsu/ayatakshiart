from django.db import models
from decimal import Decimal

class Category(models.Model):
    name = models.CharField(max_length=100, primary_key=True, help_text='Art category. eg Landscapes, Radharani, etc')

    def __unicode__(self):
        return self.name
    
class Medium(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __unicode__(self):
        return self.name


class CurrencyField(models.DecimalField):
    """
    Only changes output into a quantized format. Everything else is the same.
    """
    def __init__(self, *args, **kwargs):
        kwargs['max_digits'] =  8
        kwargs['decimal_places'] = 2
        super(CurrencyField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        try:
            return super(CurrencyField, self).to_python(value).quantize(Decimal('0.01'))
        except AttributeError:
            return None


class PrintSize(models.Model):
    print_size = models.CharField(max_length=50, primary_key=True)
    price = CurrencyField()
        
    def __unicode__(self):
        return self.print_size
    
class GalleryImage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    category = models.ForeignKey(Category)
    medium = models.ForeignKey(Medium)
    
    gallery_img_large = models.ImageField(upload_to='large_gallery_imgs/')
    gallery_img_small = models.ImageField(upload_to='small_gallery_imgs/')
    
    
    '''CATEGORIES = (
        ('Oil', 'Oil'),
        ('Water Color', 'Water Color'),
        ('Pen', 'Pen'),
        ('Pencil', 'Pencil'),
    )
    category = models.CharField(max_length=50, choices=CATEGORIES)'''
    
    
    
        
    def __unicode__(self):
        return self.name
    
