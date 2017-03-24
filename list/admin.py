from django.contrib import admin
from .models import list

admin.site.register(list)

class listAdmin(admin.ModelAdmin):
    list_display = ('list_name')
# Register your models here.
