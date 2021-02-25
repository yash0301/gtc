from django.contrib import admin
from django.db import models
from .models import GTCStack
from advanced_filters.admin import AdminAdvancedFiltersMixin


@admin.register(GTCStack)
class GTCAdmin(AdminAdvancedFiltersMixin, admin.ModelAdmin):
    list_display = ('name', 'contact_no', 'salary', 'exp', 'location', 'remarks', 'file')
    search_fields = ['job_profile', 'location', 'salary', 'exp']
    list_filter = ('job_profile', 'location', 'salary', 'exp')

    advanced_filter_fields = (
        'job_profile',
        'location',
        'salary',
        'exp'
    )