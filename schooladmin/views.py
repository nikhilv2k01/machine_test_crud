from django.shortcuts import render
from common.models import AdminLogin

from schooladmin.models import AddStudent

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse



# Create your views here.

def student_list(request):

    student_list=AddStudent.objects.all()

    return render(request, "schooladmin/student_listing.html",{"student_list":student_list,})

def register_student(request):

    if request.method=="POST":

        fname=  request.POST["fname"]
        contact=  request.POST["contact"]
        username=  request.POST["username"]
        password=  request.POST["password"]

        student_exist=AddStudent.objects.filter(username=username).exists()
        if not student_exist:

            add_student=AddStudent(fname=fname,phone=contact,username=username,password=password)
            add_student.save()
            add='Student added successfull'
            return render(request, "schooladmin/register_student.html",{'add':add,})
        else:
            msg="Username already exists"
            return render(request, "schooladmin/register_student.html",{"msg":msg})

    return render(request, "schooladmin/register_student.html")

def dashboard(request):
    dashboard=AdminLogin.objects.get(id=request.session["admin_id"])
    return render(request, 'schooladmin/dashboard.html',{"dashboard":dashboard})

@csrf_exempt
def setPermisiion(request):
    userId = request.POST["userId"]

    test = AddStudent.objects.get(id=userId)
    print(test.status)

    if test.status:
        AddStudent.objects.filter(id=userId).update(status=False)
    else:
        AddStudent.objects.filter(id=userId).update(status=True)


    return JsonResponse({'message':'Accepted permission'})
