from django.db import models

# Create your models here.


class Shedule(models.Model):
    
    day_week=models.CharField(max_length=2)
    day_active=models.BooleanField()
    duration_time=models.TimeField("%H:%M")
    begin_time=models.TimeField("%H:%M")
    end_time=models.TimeField("%H:%M")
    visits=models.CharField(max_length=5)