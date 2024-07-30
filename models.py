from django.db import models

# Create your models here.

class Registration(models.Model):
    rid=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=200)
    emailid=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    zipcode=models.CharField(max_length=200)
    contact=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    password1=models.CharField(max_length=200)
    
    class Meta:
        db_table="registration"
        
class Feedback(models.Model):
    fullname=models.CharField(max_length=200)
    emailid=models.CharField(max_length=200)
    message=models.CharField(max_length=200)
    
    class Meta:
        db_table="feedback"
        
class Bookinggas(models.Model):
    id=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=200)
    emailid=models.CharField(max_length=200)
    bookingdate=models.CharField(max_length=200)
    consumerid=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    zipcode=models.CharField(max_length=200)
    contactno=models.CharField(max_length=200)
    rid=models.IntegerField(default=0)
    
    class Meta:
        db_table="bookingas"
        
class Kycupload(models.Model):
    adharno=models.CharField(max_length=200)
    panno=models.CharField(max_length=200)
    rashancard=models.CharField(max_length=200)  
    
    class Meta:
        db_table="kycupload"  
        

    