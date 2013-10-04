from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('schools.urls', namespace="schools")),
    url(r'^classifieds/', include('classifieds.urls', namespace="classifieds")),

)
    # Examples:
    # url(r'^$', 'csquared.views.home', name='home'),
    # url(r'^csquared/', include('csquared.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

