from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Suchergebnis/(?P<data>.*)$', views.search_result, name='search_result'),
    url(r'^Profil/$', views.profile, name='profile'),
]
