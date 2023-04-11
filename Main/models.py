from django.db import models

# Create your models here.
class faculty_login(models.Model):
    fuser=models.CharField(max_length=100)
    fpass=models.CharField(max_length=100)
    
    def __str__(self):
        return self.fuser

class students(models.Model):
    sname=models.CharField(max_length=100)
    rollno=models.CharField(max_length=100)
    spass=models.CharField(max_length=100)
    marks=models.IntegerField()
    
    def __str__(self):
        return 'Rollno = '+ self.rollno+ ',' + 'Name = '+ self.sname
        # return 'Rollno = '+ self.rollno+ ' ' + 'Name = '+ self.sname+ ' ' + 'Password = '+ self.spass+ ' ' + 'Marks = '+ self.rollno
    