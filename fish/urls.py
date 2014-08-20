from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^new_tweet/$', 'fish.views.new_tweet', name='fish_new_tweet'),
    url(r'^handle_translation/$', 'fish.views.handle_translation', name='fish_handle_translation'),

)