from django.contrib import admin
from .models import Memberlist

class Memberview(admin.ModelAdmin):
    fieldsets = (
        ('名前', {
            'fields': ('memname',)
        }),
        ('概要' , {
            'fields': ('display','orderid', 'image', 'position', 'itself',)
        }),
    )
    list_display = ('memname','display','orderid', 'position', 'itself',)

admin.site.register(Memberlist, Memberview)
