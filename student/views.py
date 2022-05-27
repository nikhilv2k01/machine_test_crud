from turtle import update
from django.shortcuts import redirect, render
from pkg_resources import require

from schooladmin.models import AddStudent

# Create your views here.

def dashboard(request):
    dashboard=AddStudent.objects.get(id=request.session["user_id"])
    
    return render(request, "student/dashboard.html",{"student_dashboard":dashboard})
    


def update_student(request):
    update_student=AddStudent.objects.get(id=request.session["user_id"])

    if request.method=="POST":
        fname=request.POST["fname"]
        phone=request.POST["contact"]
        username=request.POST["username"]
        password=request.POST["password"]

        update_student.fname=fname
        update_student.phone=phone
        update_student.username=username
        update_student.password=password
        update_student.save()

        return redirect("student:dashboard")


    return render(request, "student/update_student.html",{"update_student":update_student})
    