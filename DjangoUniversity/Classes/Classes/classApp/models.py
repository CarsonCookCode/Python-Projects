from django.db import models

class DjangoClasses(models.Model):
    title = models.CharField(max_length=50)
    courseNumber = models.IntegerField()
    instructorName = models.CharField(max_length=50)
    duration = models.FloatField()
