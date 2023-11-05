from django.db import models

# Create your models here.
class Leave(models.Model):
    name = models.CharField(max_length=255)
    RegNo = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    Course = models.CharField(max_length=255)
    Date_Time = models.CharField(max_length=255)
    Destination = models.CharField(max_length=255)
    Purpose = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    time_added = models.DateTimeField(auto_now_add=True)
    Aprove = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
