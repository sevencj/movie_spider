from django.conf.urls import url

from movie import views

urlpatterns = [
    url(r'^$', views.movie_view),
    url(r'^index/$', views.index2_view)
]