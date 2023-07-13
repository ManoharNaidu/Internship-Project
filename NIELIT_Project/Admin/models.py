from django.db import models

# Create your models here.
class Admin(models.Model):
    username = models.CharField(max_length=1000)
    firstname = models.CharField(max_length=1000)
    lastname = models.CharField(max_length=1000)
    mail = models.EmailField(max_length=1000)
    phone = models.IntegerField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return "%s %s" %(self.firstname, self.lastname)
    
class Role(models.Model):
    name = models.CharField(max_length=1000,default="Trainee")

    def __str__(self):
        return "%s" %(self.name)

class Employee(models.Model):
    username = models.CharField(max_length=1000,null=False,unique=True)
    firstname = models.CharField(max_length=1000,null=False)
    lastname = models.CharField(max_length=1000)
    salary = models.IntegerField(default=0)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    mail = models.EmailField(max_length=1000)
    phone = models.IntegerField()
    hire_date = models.DateField()
    password = models.CharField(max_length=100)


    def __str__(self):
        return "%s %s, %s" %(self.firstname, self.lastname, self.role)
    


