#-*-coding:utf-8-*-
from django.conf.urls import url

from work import views

urlpatterns=[
    url(r'^login/$',views.login_view),
    url(r'^index/$',views.index_view),
    url(r'^nav.html$',views.nav_view),

]