from django.urls import path

from . import views

urlpatterns = [
    path("", views.create_employee, name="index"),
    path("employee_list/", views.employee_list),
    path("edit/<pk>/", views.edit_employee),
    path("delete/<pk>/", views.delete, name="delete"),
]
