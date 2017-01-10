# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ContactDetail'
        db.create_table(u'hello_contactdetail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('birth_day', self.gf('django.db.models.fields.DateField')()),
            ('bio', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('jabber', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('other_contacts', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'hello', ['ContactDetail'])


    def backwards(self, orm):
        # Deleting model 'ContactDetail'
        db.delete_table(u'hello_contactdetail')


    models = {
        u'hello.contactdetail': {
            'Meta': {'object_name': 'ContactDetail'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'birth_day': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['hello']