from django.db import models
from Users.models import User
# Create your models here.




class Dentists(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=155)
    description = models.TextField()
    age =  models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





class Clinic(models.Model):
    name = models.CharField(max_length=155)
    age = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=355)
    dentists = models.ManyToManyField(Dentists)

    




class WorkingHours(models.Model):
    dentists = models.ForeignKey(Dentists, on_delete=models.CASCADE)
    day = models.DateField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)