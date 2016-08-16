from django.db import models
from bolao_info.models import GPInfo, PilotInfo
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone


DEFAULT_PILOT_ID = 1


class UserBet(models.Model):
    # Who
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=DEFAULT_PILOT_ID)
    # When
    date = models.DateTimeField(default=timezone.now)
    # Where
    GPrix = models.ForeignKey(GPInfo, on_delete=models.CASCADE)
    
    # Bet
    pole = models.ForeignKey(PilotInfo, on_delete=models.PROTECT, related_name='pole', blank=True, null=True,
        limit_choices_to={'active': True})
    p1 = models.ForeignKey(PilotInfo, on_delete=models.PROTECT, related_name='p1', blank=True, null=True,
        limit_choices_to={'active': True})
    p2 = models.ForeignKey(PilotInfo, on_delete=models.PROTECT, related_name='p2', blank=True, null=True,
        limit_choices_to={'active': True})
    p3 = models.ForeignKey(PilotInfo, on_delete=models.PROTECT, related_name='p3', blank=True, null=True,
        limit_choices_to={'active': True})
    p4 = models.ForeignKey(PilotInfo, on_delete=models.PROTECT, related_name='p4', blank=True, null=True,
        limit_choices_to={'active': True})
    p5 = models.ForeignKey(PilotInfo, on_delete=models.PROTECT, related_name='p5', blank=True, null=True,
        limit_choices_to={'active': True})
    p6 = models.ForeignKey(PilotInfo, on_delete=models.PROTECT, related_name='p6', blank=True, null=True,
        limit_choices_to={'active': True})
    p7 = models.ForeignKey(PilotInfo, on_delete=models.PROTECT, related_name='p7', blank=True, null=True,
        limit_choices_to={'active': True})
    p8 = models.ForeignKey(PilotInfo, on_delete=models.PROTECT, related_name='p8', blank=True, null=True,
        limit_choices_to={'active': True})
    p9 = models.ForeignKey(PilotInfo, on_delete=models.PROTECT, related_name='p9', blank=True, null=True,
        limit_choices_to={'active': True})
    p10 = models.ForeignKey(PilotInfo, on_delete=models.PROTECT, related_name='p10', blank=True, null=True,
        limit_choices_to={'active': True})

    def get_absolute_url(self):
        return reverse('F1Bet:make-post', args=(self.id,))
    
    def __str__(self):
        return self.GPrix.country + self.GPrix.year.__str__()
