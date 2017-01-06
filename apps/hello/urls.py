from django.conf.urls import patterns, url

from apps.hello import views

urlpatterns = patterns(
    '',
    url(r'^$', views.contact_detail, name='contact_detail'),
)
