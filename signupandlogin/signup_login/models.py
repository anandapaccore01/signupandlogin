from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.management.commands.createsuperuser import Command as superuserCommand
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Command(superuserCommand):
    def handle(self, *args, **options):
        username = options.get('username')
        email = options.get('email')

        first_name = options.get('first_name')
        last_name = options.get('last_name')
        date_of_birth = options.get('date_of_birth')

        if not username:
            raise ValueError("Username must be provided.")
        if not email:
            raise ValueError("Email must be provided.")
        
        user_data={
            'username':username,
            'email':email,
            'first_name':first_name,
            'last_name':last_name,
            'date_of_birth':date_of_birth,
        }

        CustomUsers.objects.create_superuser(**user_data)

    

class CustomUsers(AbstractUser):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(unique = True, max_length=255, blank=True, null=True)
    date_of_birth = models.DateField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.CharField(unique= True, max_length=255)    
    password = models.CharField(max_length=255,  validators=[MinLengthValidator(8)])    
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=20, default='Inactive') 
    verify_string = models.CharField(max_length=50, blank=True, null=True)    
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    updated_at = models.DateTimeField( auto_now=True, blank=True, null=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name", 'last_name','date_of_birth']

  

    def __str__(self):
        return self.first_name