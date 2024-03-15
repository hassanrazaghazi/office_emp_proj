from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Employee,Role, Department
from django.db.models import Q

# Create your views here.
def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

def all_emp(request):
    emps = Employee.objects.all()
    context={
        "emps":emps,
    }
    template = loader.get_template("all_emp.html")
    return HttpResponse(template.render(context,request))

def add_emp(request):
    template = loader.get_template("add_emp.html")

    if request.method == "POST":
        first_name=request.POST["First_Name"]
        last_name=request.POST["Last_Name"]
        salary=int(request.POST["salary"])
        dept=int(request.POST["dept"])
        role=int(request.POST["role"])
        bonus=int(request.POST["bonus"])
        phone=int(request.POST["phone"])
        emp = Employee(First_Name = first_name, Last_Name = last_name, salary = salary, dept_id = dept , role_id = role, phone = phone , hire_date =datetime.now(), bonus = bonus)
        emp.save()
        return render(request,'add_emp.html')
    elif request.method == "GET":
        return render(request,"add_emp.html")
    else:
        return HttpResponse("Employee not Added Please Try again!")

    

def remove_emp(request,id=0):
    emp= Employee.objects.all()
    context={'emp':emp,}
    template = loader.get_template("remove_emp.html")

    if id:
        try:
            employee_to_be_removed = Employee.objects.get(id=id)
            employee_to_be_removed.delete()
            return HttpResponse("Employee Removed")
        except:
            return HttpResponse(template.render())
    
    
    return HttpResponse(template.render(context,request))



def filter_emp(request):
    if request.method=="POST":
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(First_Name__icontains=name) | Q(Last_Name__icontains = name))
        if dept:
            emps = emps.filter(Q(dept__name= dept))
        if role:
            emps = emps.filter(Q(role__name = role))

        context={'emps':emps,}
        return render(request,"all_emp.html",context)
    elif request.method=="GET":
        return render(request,'filter_emp.html')
    else:
        return HttpResponse("An Exception Occurred!")


    template = loader.get_template("filter_emp.html")
    return HttpResponse(template.render())