from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
]
from django.contrib import admin
from django.urls import path
from multimediaapp import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin Panel
    path('', views.index, name='dashboard'),  # Home Page
]
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from multimediaapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
