from django.contrib import admin

from .models import *


class ProjectAdmin(admin.ModelAdmin):
    pass


class Project_dateilsAdmin(admin.ModelAdmin):
    pass


class Pro_dateils_jihuaAdmin(admin.ModelAdmin):
    pass


class Pro_dateils_shijiAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(Project_dateils, Project_dateilsAdmin)
admin.site.register(Pro_dateils_jihua, Project_dateilsAdmin)
admin.site.register(Pro_dateils_shiji, Project_dateilsAdmin)
