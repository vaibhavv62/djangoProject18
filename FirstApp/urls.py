
from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_students_view),
    path("add/", views.add_student_view),
    path("update/<i>/", views.update_student_view),
    path("delete/<i>/", views.delete_student_view),
]