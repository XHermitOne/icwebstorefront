# -*- coding: utf-8 -*-


from django.contrib import admin

from . import models

class icCatalogAdmin(admin.ModelAdmin):

    list_display = ['label']

class icWareAdmin(admin.ModelAdmin):

    list_display = ['label', 'img']

admin.site.register(models.icCatalog, icCatalogAdmin)
admin.site.register(models.icWare, icWareAdmin)
