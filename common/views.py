from django.shortcuts import redirect, render

from common.models import AdminLogin
from schooladmin.models import AddStudent

# Create your views here.


def admin_login(request):
    msg = ''

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["logpass"]

        admin_exist = AdminLogin.objects.filter(
            username=username, password=password).exists()
        if admin_exist:
            admin_detail = AdminLogin.objects.get(
                username=username, password=password)

            request.session["admin_id"] = admin_detail.id

            return redirect("schooladmin:master")
        else:
            msg = "Invalid user name or password"

    return render(request, 'common/admin_login.html', {"err_msg": msg, })


def student_login(request):

    msg = ''

    if request.method == 'POST':
        username = request.POST["s_username"]
        password = request.POST["s_logpass"]
        student_exist = AddStudent.objects.filter(
            username=username, password=password,status=True).exists()
        if student_exist:

            student_detail=AddStudent.objects.get(username=username,password=password)
            request.session["user_id"]=student_detail.id
            
            return redirect("student:dashboard")
        else:
            msg = "Invalid user name or password"
            return render(request, "common/student_login.html", {"err_msg": msg, })

    return render(request, "common/student_login.html")
