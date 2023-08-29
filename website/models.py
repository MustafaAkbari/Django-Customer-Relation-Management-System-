from django.db import models

# Create your models here.

class Customer(models.Model):
    # define membership statuse
    GOLD_MEMBERSHIP = 'G'
    SILVER_MEMBERSHIP = 'S'
    BRONZE_MEMBERSHIP = 'B'
    MEMBERSHIP_CHOICES = {
        (GOLD_MEMBERSHIP, 'Gold'),
        (SILVER_MEMBERSHIP, 'Silver'),
        (BRONZE_MEMBERSHIP, 'Bronze')
    }
    MALE = "M"
    FEMALE = "F"
    GENDER_CHOICE = {
        (MALE, 'Male'),
        (FEMALE, 'Female')
    }
    date_created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE, default=MALE)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=BRONZE_MEMBERSHIP)

    # define string representation
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Address(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True, related_name='address')

    # define string representation
    def __str__(self) -> str:
        return f"{self.country} {self.city}"
