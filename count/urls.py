from django.conf.urls import patterns, url

from count import views

urlpatterns = patterns(
    '',
    url(r'^hi', views.hi, name='hi'),
    url(r'^low', views.low, name='low'),
)
