from django.contrib import admin
from .models import Footer, Related

class FooterInline(admin.TabularInline):
    model = Related

class FooterView(admin.ModelAdmin):
    fieldsets = (('Information',
                    {'fields':('active_date','active_place','member_numbers','member_charge')}),
                 ('Contact',
                    {'fields':('address_place','contact_to','mail_address')}),)
    inlines = [FooterInline]
    list_display = ('active_date','active_place','member_numbers','member_charge','address_place','contact_to','mail_address',)


admin.site.register(Footer, FooterView)

