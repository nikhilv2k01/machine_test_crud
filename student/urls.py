from . import views
from django.urls import path

app_name = "student"

urlpatterns = [
    path('update', views.update_student, name="update"),
    path('dash', views.dashboard, name="dashboard"),
]
