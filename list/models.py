from django.db import models
from django.utils import timezone

class list(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=50, null=True)
    laboratory = models.CharField(max_length=100)
    profile = models.TextField()
    phoneNumber = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    published_date = models.DateTimeField(
         blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
       return self.name
# Create your models here.
