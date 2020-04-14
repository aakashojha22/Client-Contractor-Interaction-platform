from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

from client import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('client.urls')),
    path('contractor/', include('Contractor.urls')),
              ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



admin.site.site_title = "Thekedar"
admin.site.site_header = "Thekedar Admin Login"
