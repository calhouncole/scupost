from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('schools.urls', namespace="school")),
    url(r'^classifieds/', include('classifieds.urls', namespace="classifieds")),


)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # Examples:
    # url(r'^$', 'csquared.views.home', name='home'),
    # url(r'^csquared/', include('csquared.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

