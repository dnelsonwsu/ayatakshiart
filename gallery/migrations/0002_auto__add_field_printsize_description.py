# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PrintSize.description'
        db.add_column('gallery_printsize', 'description',
                      self.gf('django.db.models.fields.TextField')(default='blah', max_length=300),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PrintSize.description'
        db.delete_column('gallery_printsize', 'description')


    models = {
        'gallery.category': {
            'Meta': {'object_name': 'Category'},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'})
        },
        'gallery.galleryimage': {
            'Meta': {'object_name': 'GalleryImage'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'gallery_img_large': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'gallery_img_small': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medium': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Medium']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'gallery.medium': {
            'Meta': {'object_name': 'Medium'},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'})
        },
        'gallery.printsize': {
            'Meta': {'object_name': 'PrintSize'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'print_size': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'})
        }
    }

    complete_apps = ['gallery']