from django.contrib import admin
from .models import *


class Operation_logAdmin(admin.ModelAdmin):
    pass

admin.site.register(Opeartion_log,Operation_logAdmin)

