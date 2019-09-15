from django.contrib import admin
from .models import About
# Register your models here.


class AboutAdmin(admin.ModelAdmin):
    list_per_page = 25


admin.site.register(About, AboutAdmin)
