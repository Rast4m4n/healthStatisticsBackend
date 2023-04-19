from django.contrib import admin

from .filters import (AgeThenFilter, GenderFilter, QuantityStepsFilter,
                      UsersWithGoodActivity)
from .models import *


class HealthAdmin(admin.ModelAdmin):
    list_filter = (QuantityStepsFilter, AgeThenFilter,
                   GenderFilter, UsersWithGoodActivity,)


class UserAdmin(admin.ModelAdmin):
    search_fields = ('id', 'email')


admin.site.register(Health, HealthAdmin)
admin.site.register(User, UserAdmin)
