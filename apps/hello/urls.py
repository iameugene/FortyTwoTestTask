from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from apps.hello import views

urlpatterns = patterns(
    '',
    url(r'^$', views.contact_detail, name='contact_detail'),
    url(r'^requests/$', TemplateView.as_view(
        template_name='hello/request_list.html'), name="request_list"),
)
