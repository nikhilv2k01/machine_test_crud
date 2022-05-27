from . import views
from django.urls import path

app_name = "common"

urlpatterns = [
    path('', views.admin_login, name="admin_login"),
    path('stdlog', views.student_login, name="student_login"),
]
