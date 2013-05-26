# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('gallery_category', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, primary_key=True)),
        ))
        db.send_create_signal('gallery', ['Category'])

        # Adding model 'Medium'
        db.create_table('gallery_medium', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, primary_key=True)),
        ))
        db.send_create_signal('gallery', ['Medium'])

        # Adding model 'PrintSize'
        db.create_table('gallery_printsize', (
            ('print_size', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
        ))
        db.send_create_signal('gallery', ['PrintSize'])

        # Adding model 'GalleryImage'
        db.create_table('gallery_galleryimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Category'])),
            ('medium', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Medium'])),
            ('gallery_img_large', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('gallery_img_small', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('gallery', ['GalleryImage'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('gallery_category')

        # Deleting model 'Medium'
        db.delete_table('gallery_medium')

        # Deleting model 'PrintSize'
        db.delete_table('gallery_printsize')

        # Deleting model 'GalleryImage'
        db.delete_table('gallery_galleryimage')


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
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'print_size': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'})
        }
    }

    complete_apps = ['gallery']