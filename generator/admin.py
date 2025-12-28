"""
Admin configuration for Headcanon Generator
"""

from django.contrib import admin
from .models import VisitorLog, PageView


@admin.register(VisitorLog)
class VisitorLogAdmin(admin.ModelAdmin):
    list_display = [
        'ip_address', 'referrer', 'landing_page',  'country', 'city', 'device_type',
        'browser', 'is_bot', 'total_visits', 'total_page_views', 'last_visit'
    ]
    list_filter = ['device_type', 'is_bot', 'is_mobile', 'country']
    search_fields = ['ip_address', 'country', 'city', 'browser', 'referrer']
    readonly_fields = ['first_visit', 'last_visit']
    ordering = ['-last_visit']


@admin.register(PageView)
class PageViewAdmin(admin.ModelAdmin):
    list_display = ['url', 'page_title', 'ip_address', 'device_type', 'country_code', 'timestamp']
    list_filter = ['device_type', 'country_code', 'method']
    search_fields = ['url', 'ip_address']
    readonly_fields = ['timestamp']
    ordering = ['-timestamp']
