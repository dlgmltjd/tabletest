from django.db import models


class Department(models.Model):
    id = models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=25)

class Person(models.Model):
    id = models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    department = models.ForeignKey(
        Department, related_name="department_members", on_delete=models.CASCADE
    )