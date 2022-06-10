from django.urls import path
from .views import index, computers,update_computer, delete_computer,users, instances,update_instance, delete_instance,users,reports

app_name = 'app'

urlpatterns = [
    path('', index, name='index'),
    path('users/', users, name='users'),
    path('reports/', reports, name='reports'),
    path('computers/', computers, name='computers'),
    path('update_computer/<pk>', update_computer, name="update_computer"),
    path('delete_computer/<pk>', delete_computer, name="delete_computer"),

    path('instances/', instances, name='instances'),
    path('update_instance/<pk>', update_instance, name="update_instance"),
    path('delete_instance/<pk>', delete_instance, name="delete_instance"),
]
