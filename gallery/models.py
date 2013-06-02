from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, primary_key=True, help_text='Art category. eg Landscapes, Radharani, etc')

    def __unicode__(self):
        return self.name
    
class Medium(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __unicode__(self):
        return self.name



class PrintSize(models.Model):
    print_size = models.CharField(max_length=50, primary_key=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField(max_length=300)
    
    def __unicode__(self):
        return self.print_size
    
class GalleryImage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    category = models.ForeignKey(Category)
    medium = models.ForeignKey(Medium)
    
    gallery_img_large = models.ImageField(upload_to='large_gallery_imgs/')
    gallery_img_small = models.ImageField(upload_to='small_gallery_imgs/')
    
    
    def image_thumb(self):
        if self.gallery_img_small:
            return '<img src="/media/%s" width="100" height="100" />' % (self.gallery_img_small)
        else:
            return '(Sin imagen)'
    image_thumb.allow_tags = True
    image_thumb.short_description = 'Gallery Picture'
    
    name.admin_order_field='medium'
    
    '''CATEGORIES = (
        ('Oil', 'Oil'),
        ('Water Color', 'Water Color'),
        ('Pen', 'Pen'),
        ('Pencil', 'Pencil'),
    )
    category = models.CharField(max_length=50, choices=CATEGORIES)'''
    
    
    
        
    def __unicode__(self):
        return self.name
    
