# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Pricebuysell.btce_buyprice_ltc'
        db.delete_column(u'btc_pricebuysell', 'btce_buyprice_ltc')

        # Deleting field 'Pricebuysell.btce_buyprice'
        db.delete_column(u'btc_pricebuysell', 'btce_buyprice')

        # Adding field 'Pricebuysell.btcchina_buyprice'
        db.add_column(u'btc_pricebuysell', 'btcchina_buyprice',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pricebuysell.huobi_buyprice'
        db.add_column(u'btc_pricebuysell', 'huobi_buyprice',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pricebuysell.btcchina_buyprice_ltc'
        db.add_column(u'btc_pricebuysell', 'btcchina_buyprice_ltc',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pricebuysell.huobi_buyprice_ltc'
        db.add_column(u'btc_pricebuysell', 'huobi_buyprice_ltc',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Pricebuysell.btce_buyprice_ltc'
        db.add_column(u'btc_pricebuysell', 'btce_buyprice_ltc',
                      self.gf('django.db.models.fields.FloatField')(default=0.0),
                      keep_default=False)

        # Adding field 'Pricebuysell.btce_buyprice'
        db.add_column(u'btc_pricebuysell', 'btce_buyprice',
                      self.gf('django.db.models.fields.FloatField')(default=datetime.datetime(2014, 8, 13, 0, 0)),
                      keep_default=False)

        # Deleting field 'Pricebuysell.btcchina_buyprice'
        db.delete_column(u'btc_pricebuysell', 'btcchina_buyprice')

        # Deleting field 'Pricebuysell.huobi_buyprice'
        db.delete_column(u'btc_pricebuysell', 'huobi_buyprice')

        # Deleting field 'Pricebuysell.btcchina_buyprice_ltc'
        db.delete_column(u'btc_pricebuysell', 'btcchina_buyprice_ltc')

        # Deleting field 'Pricebuysell.huobi_buyprice_ltc'
        db.delete_column(u'btc_pricebuysell', 'huobi_buyprice_ltc')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'btc.btcexchange': {
            'Meta': {'object_name': 'Btcexchange'},
            'btcamount': ('django.db.models.fields.FloatField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 8, 13, 0, 0)', 'blank': 'True'}),
            'exchange_coin': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'exchange_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'exchange_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'website': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'})
        },
        u'btc.pricebuysell': {
            'Meta': {'object_name': 'Pricebuysell'},
            'bitfinex_buyprice': ('django.db.models.fields.FloatField', [], {}),
            'bitfinex_buyprice_ltc': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'btcchina_buyprice': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'btcchina_buyprice_ltc': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 8, 13, 0, 0)', 'blank': 'True'}),
            'huobi_buyprice': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'huobi_buyprice_ltc': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'okcoin_buyprice': ('django.db.models.fields.FloatField', [], {}),
            'okcoin_buyprice_ltc': ('django.db.models.fields.FloatField', [], {'default': '0.0'})
        },
        u'btc.userprofile': {
            'BTCE2okCoin': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'Meta': {'object_name': 'Userprofile'},
            'amount': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'auto_trade': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'bitfinex2btcchina': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'bitfinex2btce': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'bitfinex2huobi': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'bitfinex2okCoin': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'bitfinex_key': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '65'}),
            'bitfinex_secret': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '65'}),
            'btcchina2bitfinex': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'btcchina2huobi': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'btcchina2okCoin': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'btcchina_key': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '65'}),
            'btcchina_secret': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '65'}),
            'btce2bitfinex': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'btce_key': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '65'}),
            'btce_secret': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '65'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 8, 13, 0, 0)', 'blank': 'True'}),
            'huobi2bitfinex': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'huobi2btcchina': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'huobi2okCoin': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'huobi_key': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '65'}),
            'huobi_secret': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '65'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'okCoin2BTCE': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'okCoin2bitfinex': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'okCoin2btcchina': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'okCoin2huobi': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'okcoin_key': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '65'}),
            'okcoin_secret': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '65'}),
            'rate': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['btc']