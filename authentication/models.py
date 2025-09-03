from django.db import models

class User(models.Model):
    ROLE_CHOICES = [
        ("customer", "Customer"),
        ("supplier", "supplier"),
        ("vendor", "vendor"),
        ("analyst","analyst")
    ]

    AUTH_METHOD_CHOICES = [
        ("google", "Google"),
        ("email", "Email"),
    ]

    id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255)  
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="customer")
    auth_method = models.CharField(max_length=20, choices=AUTH_METHOD_CHOICES, default="email")

    def __str__(self):
        return f"{self.name} ({self.email})"
