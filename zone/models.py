from django.db import models


# Create your models here.


class Form(models.Model):
    fname = models.CharField(max_length= 120)    
    lname =  models.CharField(max_length= 120)
    email = models.CharField(max_length= 120)
    # dob = models.DateField()
    date = models.DateField()
    


    def __str__(self):
        return self.fname
    


