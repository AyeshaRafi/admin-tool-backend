from django.contrib import admin
from homefeed.models import HomefeedElement
# Register your models here.

class HomefeedElementAdmin(admin.ModelAdmin):
    """Customize admin portal for user model"""

    list_display = ("uuid", "title", "order", "is_active")


admin.site.register(HomefeedElement, HomefeedElementAdmin)