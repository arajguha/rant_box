from django.contrib import admin
from . import models


admin.site.register(models.RantPost)
admin.site.register(models.PostReact)
admin.site.register(models.CategoryOption)