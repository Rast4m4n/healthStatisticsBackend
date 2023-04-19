from django.db import models


class User(models.Model):
    email = models.EmailField(null=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.email} пол: {self.gender} возраст: {self.age}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = "Users"


class Health(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    steps = models.IntegerField()
    minutesWalk = models.IntegerField()
    burnedEnergy = models.IntegerField()
    dateTimeActivity = models.DateTimeField()

    def __str__(self):
        return f'{self.steps} шагов {self.minutesWalk} 'f'минут ходьбы {self.burnedEnergy} калорий потрачено'

    class Meta:
        verbose_name = 'Health'
        verbose_name_plural = "Healths"