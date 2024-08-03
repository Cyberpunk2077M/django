from django.contrib import admin
from .models import cartype,Car_Review, dealership, regno
# Register your models here.
class reviewinline(admin.TabularInline):
    model= Car_Review
    extra= 2

class cartypeadmin(admin.ModelAdmin):
    list_display= ('name','brand','power', 'type', 'sold_date')
    inlines= [reviewinline]

class dealershipadmin(admin.ModelAdmin):
    list_display= ('name','location')
    filter_horizontal= ("carname",)

class regnoadmin(admin.ModelAdmin):
    list_display= ('car', 'reg_no', 'reg_date')
    

admin.site.register(cartype, cartypeadmin)
admin.site.register(dealership, dealershipadmin)
admin.site.register(regno, regnoadmin)