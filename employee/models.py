from django.db import models

class Employee(models.Model):
    emp_name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=255, null=False)
    phone = models.BigIntegerField(null=False)

    def go_to_link_edit(self):
        return f"/edit/{self.id}/"

    def go_to_link_delete(self):
        return f"/delete/{self.id}/"

    def __str__(self):
        return self.emp_name
