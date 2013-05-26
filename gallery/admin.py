from django.contrib import admin
import gallery.models

admin.site.register(gallery.models.GalleryImage)
admin.site.register(gallery.models.Medium)
admin.site.register(gallery.models.Category)
admin.site.register(gallery.models.PrintSize)
