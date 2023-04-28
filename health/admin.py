from django.contrib import admin

from .filters import (AgeThenFilter, GenderFilter, QuantityStepsFilter,
                      UsersWithGoodActivity)
from .models import *


class HealthAdmin(admin.ModelAdmin):
    list_filter = (QuantityStepsFilter,  UsersWithGoodActivity,)


class UserAdmin(admin.ModelAdmin):
    search_fields = ('id', 'email')
    list_filter = (GenderFilter, AgeThenFilter,)


admin.site.register(Health, HealthAdmin)
admin.site.register(User, UserAdmin)
