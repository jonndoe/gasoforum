# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from main_app.models import GasTheme,\
    GasTopic,\
    GasThemeText,\
    GasTopicText,\
    GasThemeComment,\
    GasTopicComment,\
    PhotoAlbum,\
    Photo

admin.site.register(GasTheme)
admin.site.register(GasTopic)
admin.site.register(GasTopicText)
admin.site.register(GasThemeText)
admin.site.register(GasThemeComment)
admin.site.register(GasTopicComment)
admin.site.register(PhotoAlbum)
admin.site.register(Photo)

