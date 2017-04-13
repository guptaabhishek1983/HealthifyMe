from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^notify/', include('notify.urls')),
    url(r'^$', include('notify.urls')),
]
