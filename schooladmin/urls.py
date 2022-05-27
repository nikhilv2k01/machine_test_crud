from . import views
from django.urls import path

app_name = "schooladmin"

urlpatterns = [
    path('stdlist', views.student_list, name="stdlist"),
    path('regstd',views.register_student,name="regstd"),
    path('dash', views.dashboard, name="dashboard"),
    path('set_permission',views.setPermisiion,name="set_permission")
]
