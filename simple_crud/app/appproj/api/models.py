from django.db import models

# Create your models here.
class Parking(models.Model):
    parking_id = models.AutoField(primary_key = True)
    parking_name = models.CharField(max_length=255)
    parking_tot_cars = models.BigIntegerField(blank=True, default=0)
    parking_created_at = models.DateTimeField(auto_now_add=True)
    parking_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str([self.parking_id, self.parking_name, self.parking_tot_cars, 
                    self.parking_created_at, self.parking_updated_at])

class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    car_idnum = models.CharField(max_length=6, default='000000')
    car_brand = models.CharField(max_length=255)
    car_model = models.CharField(max_length=255)
    car_parking_id = models.ForeignKey(Parking, related_name='cars', on_delete=models.CASCADE)
    car_is_parked = models.BooleanField(default=False)
    car_parked_at = models.DateTimeField(auto_now_add=True)
    car_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str([self.car_id, self.car_idnum, self.car_brand, self.car_model, self.car_parking_id, 
                self.car_is_parked, self.car_parked_at, self.car_updated_at])

class ApiTask(models.Model):
    task_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'api_task'