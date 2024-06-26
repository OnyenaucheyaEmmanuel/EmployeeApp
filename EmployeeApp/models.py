from django.db import models

# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.IntegerField()
    email = models.EmailField()
    date_of_birth = models.DateField()
    # job_title = models.CharField(max_length=50)
    # hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
