from django.contrib import admin
from .models import customer_details

# Register your models here.

@admin.register(customer_details)
class customer_details_view(admin.ModelAdmin):
    list_display = ('first_name','second_name','address')
