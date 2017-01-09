from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
from . import views
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'south/', views.history_view),
    url(r'^', include('apps.hello.urls', namespace='hello')),
)
urlpatterns += staticfiles_urlpatterns()
