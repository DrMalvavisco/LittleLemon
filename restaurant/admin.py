from django.contrib import admin
from .models import Menu, Booking, MenuItem
# Register your models here.
admin.site.register(Booking)
admin.site.register(Menu)
admin.site.register(MenuItem)
