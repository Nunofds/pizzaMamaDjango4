from django.contrib import admin
from .models import Pattes


class PattesAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ingredients', 'vegetarienne', 'bio', 'prix')
    search_fields = ['nom']


admin.site.register(Pattes, PattesAdmin)
