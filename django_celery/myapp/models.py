from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.name}"
