from django.contrib import admin
from .models import Cafe, Barrio, Comment, Reviewer


# Register your models here.
admin.site.register(Cafe)
admin.site.register(Barrio)
admin.site.register(Comment)
admin.site.register(Reviewer)