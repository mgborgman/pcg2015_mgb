from django.contrib import admin
from . import models

admin.site.register(models.Bar)
admin.site.register(models.Beer)
admin.site.register(models.BarRating)
admin.site.register(models.BeerRating)
admin.site.register(models.BeerComment)
admin.site.register(models.BarComment)

