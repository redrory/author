from django.contrib import admin
from django.conf.urls import patterns, include, url
from bubbles.views import hello, current_datetime, hours_ahead
from books import views

admin.autodiscover()

urlpatterns = patterns('',
  url(r'^hello/$', hello),
  url(r'^time/$', current_datetime),
  url(r'^search-form/$',views.search_form),
  url(r'^search/$', views.search),
  url(r'^time/plus/(\d{1,2})$', hours_ahead),
  (r'^admin/', include(admin.site.urls)),
)
