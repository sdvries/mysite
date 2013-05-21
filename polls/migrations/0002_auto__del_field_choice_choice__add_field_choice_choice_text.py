# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Choice.choice'
        db.delete_column(u'polls_choice', 'choice')

        # Adding field 'Choice.choice_text'
        db.add_column(u'polls_choice', 'choice_text',
                      self.gf('django.db.models.fields.CharField')(default='hello', max_length=200),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Choice.choice'
        raise RuntimeError("Cannot reverse this migration. 'Choice.choice' and its values cannot be restored.")
        # Deleting field 'Choice.choice_text'
        db.delete_column(u'polls_choice', 'choice_text')


    models = {
        u'polls.choice': {
            'Meta': {'object_name': 'Choice'},
            'choice_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['polls.Poll']"}),
            'votes': ('django.db.models.fields.IntegerField', [], {})
        },
        u'polls.poll': {
            'Meta': {'object_name': 'Poll'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['polls']