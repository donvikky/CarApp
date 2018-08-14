from django.contrib import admin
from cars.models import (Make, Model, DrivingCondition, Colour, Cylinder, Transmission, Fuel, Drive,
                         EngineType, BodyStyle, Damage, Location, Car, CarPhoto)
# Register your models here.
admin.site.register(Make)
admin.site.register(Model)
admin.site.register(DrivingCondition)
admin.site.register(Colour)
admin.site.register(Cylinder)
admin.site.register(Transmission)
admin.site.register(Fuel)
admin.site.register(Drive)
admin.site.register(EngineType)
admin.site.register(BodyStyle)
admin.site.register(Damage)
admin.site.register(Location)
admin.site.register(Car)
admin.site.register(CarPhoto)
