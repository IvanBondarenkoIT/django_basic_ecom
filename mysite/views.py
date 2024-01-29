from django.http import HttpResponse
from django.shortcuts import render

from employees.models import Employee


def home(request):
    _employees = Employee.objects.all()
    content = {"employees": _employees}
    return render(request, "home.html", context=content)
