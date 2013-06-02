from django.contrib import admin
import gallery.models


from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe

class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name=str(value)
            output.append(u' <a href="%s" target="_blank"><img src="%s" alt="%s" /></a>' % \
                (image_url, image_url, file_name, ))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))


class GalleryImageAdmin(admin.ModelAdmin):
    ordering= ('medium',)
    list_display=('name', 'medium', 'category', 'image_thumb', 'description')
    list_display_links=('name', 'image_thumb',)
    list_editable=('medium', 'category')
    
    fields = ('name','medium', 'category', 'description', 'gallery_img_small', 'gallery_img_large')
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'gallery_img_small' or db_field.name == 'gallery_img_large':
            request = kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(GalleryImageAdmin,self).formfield_for_dbfield(db_field, **kwargs)

class PrintSizeAdmin(admin.ModelAdmin):
    ordering=('price',)
    list_display=('print_size', 'price', 'description')
    

admin.site.register(gallery.models.GalleryImage, GalleryImageAdmin)
admin.site.register(gallery.models.Medium)
admin.site.register(gallery.models.Category)
admin.site.register(gallery.models.PrintSize, PrintSizeAdmin)
