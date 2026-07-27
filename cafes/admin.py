from django.contrib import admin
from .models import Cafe, Barrio, Reviewer, Review, Tag


# Register your models here.
admin.site.register(Cafe)
admin.site.register(Barrio)
admin.site.register(Reviewer)
admin.site.register(Review)
admin.site.register(Tag)


