from django.db import models


class GPInfo(models.Model):
    # Where
    country = models.CharField(max_length=50)
    circuit = models.CharField(max_length=250)
    image = models.ImageField()
    
    # When
    year = models.IntegerField()
    race_number = models.IntegerField()
    fP1_date = models.DateTimeField()
    fP2_date = models.DateTimeField()
    fP3_date = models.DateTimeField()
    quali_date = models.DateTimeField()
    race_date = models.DateTimeField()
        
    # Results
    pole = models.CharField(max_length=50, blank=True)
    p1 = models.CharField(max_length=50, blank=True)
    p2 = models.CharField(max_length=50, blank=True)
    p3 = models.CharField(max_length=50, blank=True)
    p4 = models.CharField(max_length=50, blank=True)
    p5 = models.CharField(max_length=50, blank=True)
    p6 = models.CharField(max_length=50, blank=True)
    p7 = models.CharField(max_length=50, blank=True)
    p8 = models.CharField(max_length=50, blank=True)
    p9 = models.CharField(max_length=50, blank=True)
    p10 = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return 'GP ' + self.country.__str__() + ' - ' + self.year.__str__()


class PilotInfo(models.Model):
    # Where
    country = models.CharField(max_length=50)
    # Who
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=3)
    number = models.IntegerField()
    helmet = models.ImageField()
    # Status
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name.__str__()
