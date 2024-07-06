from django.db import models

# Create your models here.
class SensorReading(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    tempC = models.FloatField(null=True, blank=True)
    tempF = models.FloatField(null=True, blank=True)
    humidity = models.FloatField(null=True, blank=True)
    dsm_particle = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.timestamp} - Location: {self.location}"
    

class Location(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.name
    
class SensorType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    # Add more fields as needed (e.g., specifications)

    def __str__(self):
        return self.name

class Sensor(models.Model):
    sensor_type = models.ForeignKey('SensorType', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=50, blank=True)
    # Add more fields as needed (e.g., installation_date)

    def __str__(self):
        return f"{self.sensor_type} at {self.location}"

class HistoricalAQIData(models.Model):
    timestamp = models.DateTimeField()
    aqi = models.IntegerField()
    location = models.ForeignKey('Location', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.timestamp} - AQI: {self.aqi} - Location: {self.location}"