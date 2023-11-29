from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=50)
    addressStreet = models.CharField(max_length=50)
    addressLocality = models.CharField(max_length=50)
    addressPostcode = models.CharField(max_length=6)
    addressCity = models.CharField(max_length=50)
    IC = models.CharField(max_length=10)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def _str_(self):
        return self.name
    
class Event(models.Model):
    title = models.CharField(max_length=30)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.FloatField()
    amount = models.FloatField()

    def _str_(self):
        return self.title
