from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def create_validator(self, reqPOST):
        errors={}
        if len(reqPOST['first_name'])< 2:
            errors['first_name'] = "Name must be at least 2 characters."
        if len(reqPOST['last_name'])< 2:
            errors['last_name'] = "Name must be at least 2 characters."
        if len(reqPOST['email'])< 6:
            errors['email'] = "Name must be at least 6 characters."
        if len(reqPOST['password'])< 8:
            errors['password'] = "Name must be at least 8 characters."
        if reqPOST['password'] != reqPOST['password_conf']:
            errors['password_conf'] = "Password and password confirmation must match."
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(reqPOST['email']):
            errors['regex'] = "Email in wrong format."
        user_with_email = User.objects.filter(email = reqPOST['email'])
        if len(user_with_email) >= 1:
            errors['duplicate']="Email taken, please use another."
        return errors

    def edit_validator(self, reqPOST, user_id):
        errors={}
        users_with_email = User.objects.filter(email=reqPOST['email']) #this will return a list, hence the next line using length
        if len(users_with_email)>=1:
            if user_id != users_with_email[0].id:
                errors['unique'] = "Email already taken."
        if len(reqPOST['first_name']) < 2:
            errors['name'] = "First name is too short, please use at least two characters."
        if len(reqPOST['last_name']) < 2:
            errors['last_name'] = "Last name is too short, please use at least two characters."
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(reqPOST['email']):
            errors['regex'] = "Email in wrong format."
        return errors

class PlantManager(models.Manager):
    def basic_validator(self, reqPOST):
        errors={}
        if len(reqPOST['name']) < 2:
            errors['name'] = "Course name must be at least 2 characters."
        if len(reqPOST['category']) < 5: 
            errors['category'] = "Category must be at least 5 characters."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    location = models.TextField(null = True)
    email = models.TextField()
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Plant(models.Model):
    # the related_name field becomes a new attribute of User class
    # so growing_plants = list of plants the associated user is growing
    users_growing = models.ManyToManyField(User, related_name = "growing_plants")
    category = models.CharField(max_length = 45)
    name = models.CharField(max_length = 45)
    latin_name = models.CharField(max_length = 45, null=True)
    sun = models.CharField(max_length = 45, null=True)
    water = models.CharField(max_length = 255, null=True)
    spacing = models.CharField(max_length = 45, null=True)
    height_width = models.CharField(max_length = 45, null=True)
    days_to_harvest = models.CharField(max_length = 45, null=True)
    pH = models.CharField(max_length = 45, null=True)
    planting = models.TextField(null = True)
    family=models.CharField(max_length = 45, null=True)
    soil_reqs = models.TextField(null = True)
    companion_plants = models.TextField(null = True)
    dont_plant_near = models.TextField(null = True)
    pruning = models.TextField(null = True)
    harvesting = models.TextField(null = True)
    common_pests = models.TextField(null = True)
    medicinal_props = models.TextField(null = True)
    edibility = models.TextField(null = True)
    other_uses = models.TextField(null = True)
    specific_notes = models.TextField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PlantManager() 
