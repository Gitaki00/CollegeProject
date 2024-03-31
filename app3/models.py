from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class FormData(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phno = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    purpose = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


    def __str__(self):
        return self.name