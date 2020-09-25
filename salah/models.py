from django.db import models

# Create your models here.
class Masjid(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=100,default=None)
    fazar = models.CharField(max_length=10,default=None)
    zohar = models.CharField(max_length=10,default=None)
    asar = models.CharField(max_length=10,default=None)
    magrib = models.CharField(max_length=10,default=None)
    isha = models.CharField(max_length=10,default=None)
    juma_khutba = models.CharField(max_length=10,default=None)

    def __str__(self):
        return self.name
    
