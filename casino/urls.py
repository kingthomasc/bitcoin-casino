from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'casino.views.home', name='home'),
    # url(r'^casino/', include('casino.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/profile/$', 'user_profile.views.profile', name='home'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^$', 'casino.views.home', name='home'),
    url(r'^game/(?P<pk>\d+)/$', 'game.views.game', name='game'),
    url(r'^place_bet/(?P<pk>\d+)/$', 'game.views.bet', name='place_bet'),
    url(r'^qr/(?P<key>\w+)/$', 'django_bitcoin.views.qrcode_view', name='qr_code_image'),
    url(r'^accounts/register/$', 'user_profile.views.register', name='register'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
   )