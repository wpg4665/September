from django.shortcuts import render_to_response
from datetime import date


def index(request):
	delta = date(2015, 9, 4) - date.today()
	return render_to_response('OneYear/index.html', {'delta': delta})


def contact():
	pass