from django.contrib import admin
from .models import *
# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name', 'slug']


admin.site.register(BrandModel,BrandAdmin)
admin.site.register(CarModel)
admin.site.register(Comment)