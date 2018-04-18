from django.conf.urls import url
from . import views

urlpatterns = [
   
    url(r'^$', views.registration),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^dashboard$', views.dashboard),
    url(r'^create_wish$', views.create_wish),
    url(r'^create_wish_page$', views.create_wish_page),
    url(r'^wish_page/(?P<id>\d+)$', views.wish_page),
    url(r'^remove_wish/(?P<id>\d+)$', views.remove_wish),
    url(r'^add_wish/(?P<id>\d+)$', views.add_wish)
       
]