from django.contrib import admin
from .models import Url
from .forms import UrlForm

class UrlAdmin(admin.ModelAdmin):
    list_display=["__str__","date","update"]
    form=UrlForm

admin.site.register(Url,UrlAdmin)
