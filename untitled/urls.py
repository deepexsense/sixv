from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^sixv/', include('sixv.urls')),
    url(r'^admin/', admin.site.urls),
]

