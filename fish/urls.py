from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	#url(r'^create_account/$', 'finished.views.create_account', name='finished_create_account'),
    url(r'^add_handle/$', 'fish.views.add_handle', name='fish_add_handle'),
    url(r'^handle_translation/$', 'fish.views.handle_translation', name='fish_handle_translation'),
    # url(r'^delete_item/(.+)$', 'finished.views.delete_item', name='finished_delete_item'),
)