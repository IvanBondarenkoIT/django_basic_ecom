from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from employees.models import Employee


def employee_details(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    print(employee)
    content = {"employee": employee}
    return render(request, "employee_details.html", context=content)
    # return HttpResponseRedirect(request, "employee_details.html")
