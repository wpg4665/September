from django.conf.urls import patterns, url
from django.views.generic import RedirectView

urlpatterns = patterns('Wedding.views',
	url(r'^(|ceremony|reception|guest-info|wedding-party)$', 'main_pages'),
	url(r'^favicon\.ico$', RedirectView.as_view(url='/static/Wedding/favicon.ico')),
)
