from django.db import models


class DishesCategory(models.Model):
    """Dishes category model"""

    origin = models.CharField(
        max_length=254,
        )
    name = models.CharField(
        max_length=254,
        unique=True,
        )
    friendly_name = models.CharField(
        max_length=254,
        unique=True,
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        """ Change verbose name in admin """
        verbose_name_plural = 'Dishes Categories'


class WineCategory(models.Model):
    """Wines category model"""

    origin = models.CharField(
        max_length=254,
        )
    variety = models.CharField(
        max_length=254,
        )
    name = models.CharField(
        max_length=254,
        unique=True,
        )
    friendly_name = models.CharField(
        max_length=254,
        unique=True,
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        """ Change verbose name in admin """
        verbose_name_plural = 'Wine Categories'
