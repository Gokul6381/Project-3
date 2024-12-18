from django.contrib import admin
from .models import usersData,loginHistory,carsList,Bookings



admin.site.register(usersData)
admin.site.register(loginHistory)
admin.site.register(carsList)
admin.site.register(Bookings)