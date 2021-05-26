from django.urls import path

from api import views

urlpatterns = [
    path('', views.api_overview, name="api-overview"),
    path('task-list/', views.task_list, name="task-lists"),
    path('task-create/', views.task_create, name="task-create"),
    path('task-update/<str:pk>/', views.task_update, name="task-update"),
    path('task-delete/<str:pk>/', views.task_delete, name="task-delete"),
]
