from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import EmployeeForm
from .models import Employee


# Create your views here.
def create_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("/")
        else:
            form = EmployeeForm()
    return render(request, "index.html")


def employee_list(request):
    employees = Employee.objects.all()
    return render(request,'employee_list.html', {'employees': employees})

def edit_employee(request,pk):
    employees = Employee.objects.get(pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid:
                form.save()
                return redirect("/")
    else:
        form = EmployeeForm(instance=employees)
    return render(request, "edit.html", {"form":form})


def delete(request,pk):
    employee = Employee.objects.get(pk=pk)
    employee.delete()
    return redirect("/")
 
