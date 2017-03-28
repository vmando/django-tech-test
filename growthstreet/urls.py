from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^borrowers/', include('growthstreet.borrowers.urls',
        namespace='borrowers')),
    url(r'', views.Home.as_view())
]
