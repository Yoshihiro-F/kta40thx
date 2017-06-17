from django.contrib import admin
from .models import Planmonth, Planyear

class PlanInline(admin.TabularInline):
    model = Planmonth
    extra = 12
    max_num = 12
    list_display = ['eve_month','evently','description',]

class PlanView(admin.ModelAdmin):

    list_display = ['eve_year','pub_date','up_date']
    list_filter = ['eve_year',]
    inlines = [PlanInline]

admin.site.register(Planyear, PlanView)
