from django.db import models
import geocoder

# Create your models here.

mapbox_token = 'pk.eyJ1IjoibWFwYm94MTQ1MyIsImEiOiJja3F1dnBka2QwOGllMnBvODA5dGN2ejJmIn0.M5C9oRSB9tzmD5VrIhYp6g'

class MyMap(models.Model):
    address = models.CharField(max_length=500)
    latitude = models.FloatField(null=True,blank=True)
    longitude = models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.address

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address,key=mapbox_token)
        g = g.latlng
        self.latitude = g[0]
        self.longitude = g[1]
        return super(MyMap,self).save(*args, **kwargs)
