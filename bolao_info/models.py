from django.db import models


class PilotInfo(models.Model):
    # Where
    country = models.CharField(max_length=50)
    # Who
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=3)
    number = models.IntegerField(blank=True, null=True)
    helmet_static = models.CharField(max_length=250)
    # Status
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name.__str__()
    
    
class GPInfo(models.Model):
    # Where
    country = models.CharField(max_length=50)
    circuit = models.CharField(max_length=250)
    image_static = models.CharField(max_length=250)
    
    # When
    year = models.IntegerField()
    race_number = models.IntegerField(blank=True, null=True)
    fP1_date = models.DateTimeField()
    fP2_date = models.DateTimeField()
    fP3_date = models.DateTimeField()
    quali_date = models.DateTimeField()
    race_date = models.DateTimeField()
        
    # Results
    pole = models.ForeignKey(PilotInfo, on_delete=models.PROTECT, related_name='gp_pole', blank=True, null=True,
        limit_choices_to={'active': True})
    p1 = models.ForeignKey(PilotInfo, on_delete=models.PROTECT, related_name='gp_p1', blank=True, null=True,
        limit_choices_to={'active': True})
    p2 = models.ForeignKey(PilotInfo, on_delete=models.PROTECT, related_name='gp_p2', blank=True, null=True,
        limit_choices_to={'active': True})
    p3 = models.ForeignKey(PilotInfo, on_delete=models.PROTECT, related_name='gp_p3', blank=True, null=True,
        limit_choices_to={'active': True})
    p4 = models.ForeignKey(PilotInfo, on_delete=models.PROTECT, related_name='gp_p4', blank=True, null=True,
        limit_choices_to={'active': True})
    p5 = models.ForeignKey(PilotInfo, on_delete=models.PROTECT, related_name='gp_p5', blank=True, null=True,
        limit_choices_to={'active': True})
    p6 = models.ForeignKey(PilotInfo, on_delete=models.PROTECT, related_name='gp_p6', blank=True, null=True,
        limit_choices_to={'active': True})
    p7 = models.ForeignKey(PilotInfo, on_delete=models.PROTECT, related_name='gp_p7', blank=True, null=True,
        limit_choices_to={'active': True})
    p8 = models.ForeignKey(PilotInfo, on_delete=models.PROTECT, related_name='gp_p8', blank=True, null=True,
        limit_choices_to={'active': True})
    p9 = models.ForeignKey(PilotInfo, on_delete=models.PROTECT, related_name='gp_p9', blank=True, null=True,
        limit_choices_to={'active': True})
    p10 = models.ForeignKey(PilotInfo, on_delete=models.PROTECT, related_name='gp_p10', blank=True, null=True,
        limit_choices_to={'active': True})
    
    def __str__(self):
        return 'GP ' + self.country.__str__() + ' - ' + self.year.__str__()
