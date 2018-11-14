from django.conf.urls import url

from sixv import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]