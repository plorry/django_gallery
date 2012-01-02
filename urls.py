from django.conf.urls.defaults import *
import views

#gallery urls

urlpatterns = patterns('andrewgardner.gallery.views',
	(r'^get_image/$', 'get_image'),
)