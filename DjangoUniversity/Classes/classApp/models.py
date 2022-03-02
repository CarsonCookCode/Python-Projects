from django.db import models


# Here I define a class with attributes
class DjangoClasses(models.Model):
    title = models.CharField(max_length=50)
    courseNumber = models.IntegerField()
    instructorName = models.CharField(max_length=50)
    duration = models.FloatField()

    objects = models.Manager()

# This displays the title of the object on the admin page
    def __str__(self):
        return self.title
