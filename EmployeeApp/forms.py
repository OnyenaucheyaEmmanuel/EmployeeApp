from django import forms

from .models import *


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = (
            "first_name",
            "last_name",
            "phone",
            "email",
            "date_of_birth",
        )
