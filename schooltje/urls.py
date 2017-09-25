from django.conf.urls import url

from . import views

app_name = 'schooltje'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^richtingen$', views.richtingen, name='richtingen'),
    url(r'^wieiswie$', views.wieiswie, name='wieiswie'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^contactpost$', views.contactpost, name='contactpost'),
]