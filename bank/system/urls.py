from django.urls import path

from .views import *

urlpatterns = [
    path('version_info/', Version_info.as_view()),
    path('operation_log/', Operation.as_view()),
    path('del_system_log/', Del_system_log.as_view()),

]
