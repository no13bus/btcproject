from django.core.management.base import BaseCommand,CommandError
from btc.models import Tradedate, Tradedate_analysis

class Command(BaseCommand):
	def handle(self, *args, **options):
		datas = Tradedate.objects.all().iterator()
		for data in datas:
			mtime1 = '%s %s' % (data.mtime.split(' ')[1],data.mtime.split(' ')[0])
			data.mtime = mtime1
			data.save()
			print data.id
		# datas = Tradedate.objects.all().iterator()
		# for data in datas:
		# 	mtime1 = '%s %s' % (data.mtime, data.created_day)
		# 	data.mtime = mtime1
		# 	data.save()
		# 	print data.id

		# print "done it"