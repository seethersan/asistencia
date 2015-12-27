# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import empresa, local, area, horario, empleado

admin.site.register(empresa)
admin.site.register(local)
admin.site.register(area)
admin.site.register(horario)
admin.site.register(empleado)
