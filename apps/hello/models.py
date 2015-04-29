from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    bio = models.TextField()
    email = models.EmailField()
    jabber = models.CharField(max_length=200)
    skype = models.CharField(max_length=200)
    other_contacts = models.TextField()