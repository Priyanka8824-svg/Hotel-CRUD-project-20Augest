from django.db import models

# Create your models here.
class Hotel(models.Model):
    hid = models.IntegerField(primary_key=True)
    hotel_name = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.hid}--{self.hotel_name}--{self.address}--{self.city}'