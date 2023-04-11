from django.contrib import admin
from .models import *
# Register your models here.


class UserHealthAdmin(admin.ModelAdmin):
    search_fields = ('id', 'email',  'steps', 'minutesWalk', 'burnedEnergy', 'dateTimeActivity')
    list_filter = ('id', 'email',  'steps', 'minutesWalk', 'burnedEnergy')


admin.site.register(UserHealth, UserHealthAdmin)
