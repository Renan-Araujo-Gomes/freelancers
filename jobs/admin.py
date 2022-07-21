from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Referencias, Jobs

admin.site.register(Referencias)
admin.site.register(Jobs)