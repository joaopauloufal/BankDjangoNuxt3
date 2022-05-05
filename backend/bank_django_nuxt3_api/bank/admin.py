from django.contrib import admin

from .models import Bank, Account, Agency, Client

admin.site.register([Bank, Account, Agency, Client])
