from django.contrib import admin
from devices.models import Device

# Register your models here.

class DeviceInfo(admin.ModelAdmin):
	list_display = ('Number','Name','Amount','Donater','Price','Avaliable','LastCheckTime','Remark')
	search_fields = ('Name','Donater','Price','Avaliable')
	ordering = ('Number',)

admin.site.register(Device,DeviceInfo)
