from django.contrib import admin
from . import models


class BeerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class BarAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}



admin.site.register(models.Bar, BarAdmin)
admin.site.register(models.Beer, BeerAdmin)
admin.site.register(models.BarRating)
admin.site.register(models.BeerRating)
admin.site.register(models.BeerComment)
admin.site.register(models.BarComment)
admin.site.register(models.UserProfile)




