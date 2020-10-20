from __future__ import unicode_literals

from django.db import models


class Office(models.Model):
    """This class represents the Office model."""
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return " - ".join([self.address, self.city, self.country])


class Department(models.Model):
    """This class represents the Department model."""
    name = models.CharField(max_length=255)
    super_department = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return " - ".join([str(self.pk), self.name])


class Employee(models.Model):
    first = models.CharField(
        max_length=30, blank=True, null=True
    )
    last = models.CharField(
        max_length=30, blank=True, null=True
    )
    manager = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    office = models.ForeignKey(Office, on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return " - ".join([self.first, self.last])

    class Meta:
        verbose_name_plural = "Empleados"
        verbose_name = "Empleado"

