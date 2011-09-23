from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^hakkinda/$', 'svxconf.views.about'),
    url(r'^node/new/$', 'svxconf.views.node_new'),
    url(r'^node/edit/$', 'svxconf.views.node_edit'),
    url(r'^svxlink/start/$', 'svxconf.views.svxlink_start'),
    url(r'^svxlink/stop/$', 'svxconf.views.svxlink_stop'),
    url(r'^$', 'svxconf.views.home'),
    # url(r'^svxconf/', include('svxconf.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
