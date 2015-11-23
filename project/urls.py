"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
#from django.conf import settings
#from django.conf.urls.static import static
#from main.model import views   

#import debug_toolbar


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dvd_list/$', 'main.views.dvd_list'),
    #url(r'^main_page/$', 'main.views.main_page'),
    # url(r'^dvd_detail/(?P<pk>\d+)/$', 'main.views.dvd_detail'),
    # url(r'^api_dvd_list/$', 'main.views.api_dvd_list'),
    # url(r'^api_dvd_detail/(?P<pk>\d+)/$', 'main.views.api_dvd_detail'),

    # This works 
    url(r'^movie_list_temp/$', 'main.views.dvd_list_temp'),

    # This doesn't work because you need a sql database
    url(r'^movie_list_mysql/$', 'main.views.dvd_list_mysql'),

    #url(r'^__debug__/', include(debug_toolbar.urls)),
    #url(r'^dvd_list_cas/$', 'main.views.movie_list_cas'),
    # (r'^search/', include('haystack.urls')),
    url(r'^dvd_list_dbv/$', 'main.views.dvd_list_dbv'),
    # url(r'^dvd_list)
]
