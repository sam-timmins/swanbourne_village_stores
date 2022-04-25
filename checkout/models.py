from django.db import models


class CollectionDays(models.Model):
    """ Model for colection days """
    day = models.CharField(
        max_length=9,
        unique=True,
        blank=False,
    )

    def __str__(self):
        return f'{self.day}'
