from .models import *
from django.utils.translation import gettext_lazy as _
from django.contrib import admin


class QuantityStepsFilter(admin.SimpleListFilter):
    title = _('Количество шагов')
    parameter_name = 'steps'

    def lookups(self, request, model_admin):
        return (
            ('low', _('Меньше 5тыс. шагов')),
            ('medium', _('От 5тыс. до 15тыс. шагов')),
            ('hight', _('От 15тыс. до 25тыс. шагов')),
            ('higher', _('Больше 25тыс. шагов')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'low':
            return queryset.filter(
                steps__lte=5000,
            )
        if self.value() == 'medium':
            return queryset.filter(
                steps__lte=15000,
                steps__gte=5000,
            )
        if self.value() == 'hight':
            return queryset.filter(
                steps__lte=25000,
                steps__gte=15000,
            )
        if self.value() == 'higher':
            return queryset.filter(
                steps__gte=25000,
            )


class AgeThenFilter(admin.SimpleListFilter):
    title = _('Возраст')
    parameter_name = 'age'

    def lookups(self, request, model_admin):
        return (
            ('teenager', _('Младше 18 лет')),
            ('adult', _('Старше 18 лет')),
            ('older', _('Старше 40 лет')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'teenager':
            return queryset.filter(
                age__lte=18,
            )
        if self.value() == 'adult':
            return queryset.filter(
                age__lte=40,
                age__gte=18,
            )
        if self.value() == 'older':
            return queryset.filter(
                age__lte=40,
            )


class GenderFilter(admin.SimpleListFilter):
    title = _('Пол')
    parameter_name = 'gender'

    def lookups(self, request, model_admin):
        return (
            ('male', _('Мужской')),
            ('female', _('Женский')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'male':
            return queryset.filter(
                gender='Мужской',
            )
        if self.value() == 'female':
            return queryset.filter(
                gender='Женский',
            )
