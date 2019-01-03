from django.urls import path

from .views import *

urlpatterns = [
    path('project/', Project_View.as_view(), name='project'),
    path('pro_details/', Pro_dateils_shiji_view.as_view(), name='pro_deta'),
    path('del_project/', Del_project.as_view(), name='del_pro'),
    path('del_project_dateils/', Del_project_dateils.as_view(), name='del_pro_date'),
    path('add_project/', Add_project.as_view()),
    path('add_project_stage/', Add_project_stage.as_view()),
    path('pro_schedule/', Pro_schedule.as_view()),
    path('graph_simple/', Graph_simple.as_view()),
    path('check_start_time/', Check_start_time.as_view()),
    path('check_stop_time/', Check_stop_time.as_view()),
    path('edit_project/', Edit_project.as_view()),
    path('edit_project_stage/', Edit_project_stage.as_view()),
]
