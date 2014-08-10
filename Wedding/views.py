from collections import OrderedDict
from django.shortcuts import render_to_response
from datetime import datetime


def index(request):
	wedding_date = datetime(2015, 9, 4, 16, 30, 0)
	ordinal = lambda n: "%d%s" % (n, "tsnrhtdd"[(n / 10 % 10 != 1) * (n % 10 < 4) * n % 10::4])
	delta = wedding_date - datetime.now()
	total_hours = delta.seconds // 3600
	difference = OrderedDict({})
	difference["days"] = delta.days
	difference["hours"] = total_hours
	difference["minutes"] = (delta.seconds // 60) - (total_hours * 60)
	formatted_date = OrderedDict({})
	formatted_date["day"] = "The " + ordinal(wedding_date.day)
	formatted_date["month"] = "of " + wedding_date.strftime("%b")
	formatted_date["year"] = wedding_date.strftime("%Y")
	return render_to_response('Wedding/index.html', {'diff': difference, 'wedd_date': formatted_date})


def contact():
	pass