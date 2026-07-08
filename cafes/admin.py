from django.contrib import admin
from .models import Cafe, Barrio, Review


# Register your models here.
admin.site.register(Cafe)
admin.site.register(Barrio)
admin.site.register(Review)