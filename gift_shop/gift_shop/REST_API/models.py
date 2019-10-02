from django.db import models
from django.core.validators import int_list_validator
from datetime import datetime

GENDER_CHOISES = ['male', 'female']


class Citizens(models.Model):
    import_id = models.AutoField(primary_key=True)
    citizen_id = models.PositiveIntegerField()
    town = models.CharField(max_length=256)
    street = models.CharField(max_length=256)
    building = models.CharField(max_length=256)
    apartment = models.PositiveIntegerField()
    name = models.CharField(max_length=256)
    birth_date = models.DateField(input_formats=['%dd/%mm/%YYYY'])  # need date validator
    gender = models.CharField(choices=GENDER_CHOISES)
    relatives = models.CharField(validators=int_list_validator)

    class Meta:
        ordering = ['created']

