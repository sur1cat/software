from django.db import models
from user.models import Operators

class Course(models.Model):
    name = models.CharField(blank=False, null=False, max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f'{self.name} {self.description} {self.price}'


class ApplicationRequest(models.Model):
    user_name = models.CharField(max_length=255, null=False, blank=False)
    commentary = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    handled = models.BooleanField(default=False)
    operators = models.ManyToManyField('Operators', related_name='applications')

    def __str__(self):
        return f'{self.user_name} {self.phone}'

class ApplicationCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    application = models.ForeignKey(ApplicationRequest, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.course}'
