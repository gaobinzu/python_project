from django.urls import path

from .views import *

urlpatterns = [
    path('index/', IndexViews.as_view(), name='main'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin_list/', Admin_list.as_view(), name='admin_list'),
    path('admin_add/', Admin_add.as_view(), name='admin_add'),

]
