from django.db import models


class Operators(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    surname = models.CharField(max_length=255, blank=False, null=False)
    department = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return f'{self.name}'