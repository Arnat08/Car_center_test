from django.db import models
class Car(models.Model):
     name = models.CharField(max_length=255,blank=False,null=False)
     available=models.IntegerField(default=0)
     image=models.CharField(max_length=1000,blank=True,default="")


     def __str__(self):
          return (f"{self.id}{self.name},available: {self.available}")


class Order(models.Model):
     car = models.ForeignKey(Car, on_delete=models.CASCADE)
     name = models.CharField(max_length=255)
     email = models.CharField(max_length=255, blank=True, null=True)
     phone = models.IntegerField(default=0)
     city = models.CharField(max_length=255, blank=False, null=False)
     status = models.CharField(max_length=100,default="created")




     def __str__(self):
          return(f"{self.car},{self.name},phone:{self.phone},city:{self.city},{self.status}")


