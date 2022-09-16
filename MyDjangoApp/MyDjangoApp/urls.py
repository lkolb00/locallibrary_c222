from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('mailingsystem.urls')),
    path(r'^admin/', admin.site.urls),
    path(r'^mailingsystem/', include('mailingsystem.urls'))
]