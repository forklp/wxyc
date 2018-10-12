from django.contrib import admin
from . import models
# Register your models here.


class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_number', 'phone', 'status')
    list_filter = ('status',)
    search_fields = ('car_number',)


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'status')
    list_filter = ('status',)
    search_fields = ('name',)


admin.site.register(models.Driver, DriverAdmin)
admin.site.register(models.User, UserAdmin)