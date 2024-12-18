from django.db import models
from django.utils import timezone

class usersData(models.Model):
    name=models.CharField(max_length=50)
    phone=models.BigIntegerField()
    email=models.CharField(max_length=60)
    city=models.CharField(max_length=50)
    userId=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=500)

    def __str__(self):
        return self.userId
    
class loginHistory(models.Model):
    userId=models.CharField(max_length=20)
    password=models.CharField(max_length=16)
    validate=models.BooleanField()
    loginTime=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.userId
    
class carsList(models.Model):
    carId=models.AutoField(primary_key=True)
    ownerName=models.CharField(max_length=50)
    ownerPhone=models.BigIntegerField()
    ownerAddress=models.CharField(max_length=100)
    carModel=models.CharField(max_length=100)
    carRent=models.IntegerField()
    carImage=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.ownerName
    
class Bookings(models.Model):
    bookId=models.AutoField(primary_key=True)
    userId=models.ForeignKey(usersData,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    phone=models.BigIntegerField()
    pickup=models.CharField(max_length=150)
    pickupDate=models.DateField()
    drop=models.CharField(max_length=150)
    dropDate=models.DateField()
    car=models.ForeignKey(carsList,on_delete=models.CASCADE)
    bookingDate=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.bookId

