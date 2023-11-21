from django.db import models

# Create your models here.
from django.db import models

class District(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=50)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class AccountType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Application(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(blank=True)
    age = models.IntegerField(blank=True)
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    material = models.ManyToManyField(Material)

    def __str__(self):
        return self.name