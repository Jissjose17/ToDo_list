from django.urls import path
from todo_app import views

urlpatterns = [

    path('',views.homepage,name='homepage'),
    path('taskfunction',views.taskfunction,name='taskfunction'),
    path('deletefuntion/<int:data>',views.deletefuntion,name='deletefuntion'),
    path('editfunction/<int:data>',views.editfunction,name='editfunction'),
    path('editpage/<int:data>',views.editpage,name='editpage'),
]