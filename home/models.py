from django.db import models


class OpenHours(models.Model):
    """ Opening hours for the store """

    day = models.CharField(
        max_length=50,
        unique=True
        )
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self):
        return f'{self.day}'
