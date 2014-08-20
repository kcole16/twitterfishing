from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'fish.views.home', name='home'),
    # url(r'^create_account$', 'core.views.create_account', name='create_account'),

    url(r'^fish/', include('fish.urls')),

    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    # url(r'^handle_yoauth/', 'core.views.handle_yoauth', name='handle_yoauth'),
    url(r'^logout', 'fish.views.logout_view', name='logout'),

    url('', include('social.apps.django_app.urls', namespace='social')),
)
