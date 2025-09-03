from django.db import models

# Register your models here.
class Admin(models.Model):
    id = models.AutoField(primary_key=True) 
     
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255) 
    
    def __str__(self):
        return f"{self.name} ({self.email})" 