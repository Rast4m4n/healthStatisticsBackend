from django.db import models


class UserHealth(models.Model):
    email = models.EmailField(null=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    steps = models.IntegerField()
    minutesWalk = models.IntegerField()
    burnedEnergy = models.IntegerField()
    dateTimeActivity = models.DateField()

    def __str__(self):
        return f'{self.email} {self.steps} шагов {self.minutesWalk} минут ходьбы {self.burnedEnergy} калорий потрачено'

    class Meta:
        verbose_name = 'UserHealth'
        verbose_name_plural = "UsersHealth"
