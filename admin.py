from django.contrib import admin

from django.contrib import admin
from django.urls import path
from multimediaapp import views  # Import views from your app

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin panel
    path('', views.index, name='dashboard'),  # Your homepage (dashboard)
]
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

# Customize Admin Header
admin.site.site_header = "Multimedia Admin Panel"
admin.site.site_title = "Multimedia Dashboard"
admin.site.index_title = "Welcome to the Multimedia Dashboard"

# Create a Custom Admin View to Link to Home Page
@admin.register(admin.models.LogEntry)  # Registers the view
class CustomAdminHome(admin.ModelAdmin):
    def home_link(self):
        url = reverse('dashboard')  # Name from urls.py
        return format_html('<a href="{}" target="_blank">Go to Home Page</a>', url)

    home_link.short_description = "Visit Home Page"

    list_display = ("home_link",)

    from django.contrib import admin
from .models import Video

admin.site.register(Video)

