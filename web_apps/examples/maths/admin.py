from django.contrib import admin

# Register your models here.
from .models import Math


class AdminMath(admin.ModelAdmin):
    list_display = ['operacja', 'a', 'b', 'wynik', 'created']
    list_filter = ['operacja']
    search_fields = ['wynik']

admin.site.register(Math, AdminMath)