from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^index/$', views.index, name="index"),
    url(r'^about/$', views.about, name="about"),
    url(r'^share/$', views.share, name="share"),
    url(r'^list/$', views.list, name="list"),
    url(r'^fengmian/$', views.fengmian, name="fengmian"),
    url(r'^info/$', views.info, name="info"),
    url(r'^time/$', views.time, name="time"),

    url(r'^pic$', views.index, name='upload_pic'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)