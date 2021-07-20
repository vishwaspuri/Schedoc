from django.contrib import admin
from user import models
# Register your models here.

admin.site.site_header = "Schedoc Administration"
admin.site.register(models.User)