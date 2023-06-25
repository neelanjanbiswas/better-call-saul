from django.db import models


# Create your models here.
class info(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=5)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
    
