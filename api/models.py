from django.db import models

# Create your company models here.
class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name= models.CharField(max_length=50)
    Location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100, choices=(('IT','IT'),
                                                   ('Non IT','Non IT'),
                                                   ("Mobiles Phones",'Mobile Phones')
                                                   ))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name +'--'+ self.Location
    
#Employee Model
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)  
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)  
    about = models.TextField()
    position = models.CharField(max_length=50, choices=(
        ('manager', 'Manager'),
        ('software_developer', 'Software Developer'),  
        ('project_leader', 'Project Leader'),  
    ))
    company = models.ForeignKey('Company', on_delete=models.CASCADE)  

    def __str__(self):
        return self.name