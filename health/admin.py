from django.contrib import admin
from .models import *
from django.utils.translation import gettext_lazy as _
from .filters import *


class UserHealthAdmin(admin.ModelAdmin):
    search_fields = ('id', 'email')
    list_filter = (QuantityStepsFilter, AgeThenFilter, GenderFilter,)


admin.site.register(UserHealth, UserHealthAdmin)

