from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from .forms import RegistrationForm,DepartmentForm
from .models import Employee,Registration,Department


def indexfunction(request):
    return render(request,"index.html")

def formdemofunction(request):
    return render(request,"formdemo.html")

def displayformdatafunction(request):
    if request.method == "POST":
        id=request.POST['id']
        name=request.POST['name']
        gender = request.POST['gender']
        dateofbirth = request.POST['dateofbirth']
        department = request.POST['department']
        emailid = request.POST['emailid']
        contactno = request.POST['contactno']
        return render(request,"displayform.html",{"id":id,"name":name,"gender":gender,"dob":dateofbirth,"dept":department,"email":emailid,"contactno":contactno})
    if request.method == "GET":
        id = request.GET['id']
        name = request.GET['name']
        gender = request.GET['gender']
        dateofbirth = request.GET['dateofbirth']
        department = request.GET['department']
        emailid = request.GET['emailid']
        contactno = request.GET['contactno']
        return render(request, "displayform.html",{"id": id, "name": name, "gender": gender, "dob": dateofbirth, "dept": department,"email": emailid, "contactno": contactno})

def logindemofunction(request):
    return render(request,"logindemo.html")

def checklogindemofunction(request):
    email = request.POST['emailid']
    pwd = request.POST['password']
    if email=="klu@gmail.com" and pwd=="klu":
        return HttpResponse("<b>Login Success</b>")
    else:
        return HttpResponse("<font color=red>Login Failed</font>")

def addemployeefunction(request):
    return render(request,"addemployee.html")

def saveemployeefunction(request):
    id = request.POST['id']
    name = request.POST['name']
    gender = request.POST['gender']
    dateofbirth = request.POST['dateofbirth']
    department = request.POST['department']
    emailid = request.POST['emailid']
    contactno = request.POST['contactno']
    employeeobj = Employee(emp_id=id,emp_name=name,emp_gender=gender,emp_dob=dateofbirth,emp_dept=department,emp_email=emailid,emp_contactno=contactno)
    Employee.save(employeeobj)
    return HttpResponse("Employee Added Successfully")

def registration(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            msg="Successfully Registered"
            return render(request,"regsuccess.html",{"msg":msg})
        else:
            return HttpResponse("Registraion Failed")
    return render(request,"registration.html",{"form":form})

def userlogin(request):
    return render(request,"userlogin.html")

def checkuserlogin(request):
    emailid=request.POST["emailid"]
    pwd=request.POST["password"]

    flag=Registration.objects.filter(Q(email=emailid) & Q(password=pwd))



    if flag:
        return render(request,"userhome.html")
    else:
        msg="Login Failed"
        return render(request,"userlogin.html",{"msg":msg})

def userhome(request):
    return render(request,"userhome.html")

def userlogout(request):
    return render(request,"userlogin.html")

def viewusers(request):
    usersdata = Registration.objects.all()
    userscount = Registration.objects.count()
    return render(request,"viewusers.html",{"users":usersdata,"count":userscount})

def adddepartment(request):
    form=DepartmentForm()
    form.save()
    if request.method == "POST":
        form=DepartmentForm(request.POST)
        if form.is_valid():
            msg="Department Added Successfully"
            return render(request,"adddepartment.html",{"msg":msg,"deptform":form})
        else:
            msg="Failed to Add Department"
            return render(request, "adddepartment.html", {"msg": msg,"deptform":form})

    return render(request,"adddepartment.html",{"deptform":form})