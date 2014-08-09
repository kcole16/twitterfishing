from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	#url(r'^create_account/$', 'finished.views.create_account', name='finished_create_account'),
    url(r'^add_item/$', 'finished.views.add_item', name='finished_add_item'),
    url(r'^handle(.+)$', 'finished.views.handle', name='finished_handle'),
    url(r'^delete_item/(.+)$', 'finished.views.delete_item', name='finished_delete_item'),
)