from django.urls import path
from .import views
urlpatterns=[
    path("student/<int:student_id>",views.student_detail,name="root"),
             ]
