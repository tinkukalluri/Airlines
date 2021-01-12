from django.contrib import admin
from .models import airports,flights,passengers

class flightsAdmin(admin.ModelAdmin):
    list_display=("id","origin","destination","duration")

class passengersAdmin(admin.ModelAdmin):
    filter_horizontal=("flights6",)

admin.site.register(airports)
admin.site.register(flights,flightsAdmin)
admin.site.register(passengers,passengersAdmin)
