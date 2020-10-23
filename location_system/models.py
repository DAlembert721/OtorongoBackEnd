from django.db import models


# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'regions'


class Province(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    class Meta:
        db_table = 'provinces'


class District(models.Model):
    name = models.CharField(max_length=50)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    class Meta:
        db_table = 'districts'
