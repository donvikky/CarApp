from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Make(models.Model):
    name = models.CharField('Name', max_length=250)
    description = models.TextField('Description', blank=True, null=True)

    def __str__(self):
        return self.name


class Model(models.Model):
    make = models.ForeignKey(Make, related_name='models', on_delete=models.CASCADE)
    name = models.CharField('Name', max_length=250)
    description = models.TextField('Description', blank=True, null=True)

    def __str__(self):
        return self.name


class DrivingCondition(models.Model):
    name = models.CharField('Name', max_length=250)
    description = models.TextField('Description', null=True, blank=True)

    def __str__(self):
        return self.name


class Colour(models.Model):
    name = models.CharField('Name', max_length=250)
    description = models.TextField('Description', null=True, blank=True)

    def __str__(self):
        return self.name


class Cylinder(models.Model):
    name = models.CharField('Name', max_length=250)
    description = models.TextField('Description', null=True, blank=True)

    def __str__(self):
        return self.name


class Transmission(models.Model):
    name = models.CharField('Name', max_length=250)
    description = models.TextField('Description', null=True, blank=True)

    def __str__(self):
        return self.name


class Fuel(models.Model):
    name = models.CharField('Name', max_length=250)
    description = models.TextField('Description', null=True, blank=True)

    def __str__(self):
        return self.name


class Drive(models.Model):
    name = models.CharField('Name', max_length=250)
    description = models.TextField('Description', null=True, blank=True)

    def __str__(self):
        return self.name


class EngineType(models.Model):
    name = models.CharField('Name', max_length=250)
    description = models.TextField('Description', null=True, blank=True)

    def __str__(self):
        return self.name


class BodyStyle(models.Model):
    name = models.CharField('Name', max_length=250)
    description = models.TextField('Description', null=True, blank=True)

    def __str__(self):
        return self.name


class Damage(models.Model):
    name = models.CharField('Name', max_length=250)
    description = models.TextField('Description', null=True, blank=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField('Location', max_length=250)

    def __str__(self):
        return self.name


class Car(models.Model):
    START_MECHANISM_CHOICES = (
        ('PUSH_TO_START', 'Push to Start'),
        ('KEY_START', 'Key Start'),
    )
    KEY_CHOICES = (
        ('PRESENT', 'Present'),
        ('ABSENT', 'Absent')
    )
    STATUS_CHOICES = (
        ('AVAILABLE', 'Available'),
        ('Unavailable', 'Unavailable')
    )
    SALE_STATUS_CHOICES = (
        ('PURE_SALE', 'Pure Sale'),
        ('FIRE_SALE', 'Fire Sale')
    )
    make = models.ForeignKey(Make, related_name='make', on_delete=models.CASCADE)
    model = models.ForeignKey(Model, related_name='model', on_delete=models.CASCADE)
    year = models.PositiveSmallIntegerField('Year', validators=[MinValueValidator(1980), MaxValueValidator(2018)])
    driving_condition = models.ForeignKey(DrivingCondition, related_name='driving_condition', on_delete=models.CASCADE)
    vin = models.CharField('VIN', max_length=250)
    odometer = models.CharField('Odometer', max_length=250)
    colour = models.ForeignKey(Colour, related_name='colour', on_delete=models.CASCADE)
    cylinder = models.ForeignKey(Cylinder, related_name='cylinder', on_delete=models.CASCADE)
    transmission = models.ForeignKey(Transmission, related_name='transmission', on_delete=models.CASCADE)
    fuel = models.ForeignKey(Fuel, related_name='fuel', on_delete=models.CASCADE)
    drive = models.ForeignKey(Drive, related_name='drive', on_delete=models.CASCADE)
    engine_type = models.ForeignKey(EngineType, related_name='engine_type', on_delete=models.CASCADE)
    start_mechanism = models.CharField('Start Mechanism', max_length=250, choices=START_MECHANISM_CHOICES)
    key = models.CharField('Key', max_length=10, choices=KEY_CHOICES)
    body_style = models.ForeignKey(BodyStyle, related_name='body_style', on_delete=models.CASCADE)
    damage = models.ForeignKey(Damage, related_name='damage', on_delete=models.CASCADE)
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES)
    sale_status = models.CharField('Sale Status', max_length=20, choices=SALE_STATUS_CHOICES)
    location = models.ForeignKey(Location, related_name='location', on_delete=models.CASCADE)
    amount = models.DecimalField('Amount', max_digits=20, decimal_places=2)
    featured = models.NullBooleanField()
    feature_photo = models.ImageField('Feature', upload_to='pix', null=True, blank=True)

    def __str__(self):
        carname = "%s %s %d" % (self.make, self.model, self.year)
        return carname


class CarPhoto(models.Model):
    car = models.ForeignKey(Car, related_name='photos', on_delete=models.CASCADE)
    photo = models.ImageField('Photo', upload_to='pix', null=True, blank=True)

    def __str__(self):
        carname = "%s %s %d" % (self.car.make, self.car.model, self.car.year)
        return carname



