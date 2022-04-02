from django.db import models
from cloudinary.models import CloudinaryField

DISH_STATUS = ((0, 'Frozen'), (1, 'Fresh'))


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


class Dishes(models.Model):
    """ Model for dishes """
    category = models.ForeignKey(
        'DishesCategory',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        )
    name = models.CharField(
        max_length=254,
        unique=True,
        )
    slug_name = models.SlugField(
        max_length=254,
        unique=True,
    )
    status = models.IntegerField(
        choices=DISH_STATUS,
        default=1
        )
    image = CloudinaryField(
        'image',
        default='placeholder',
        null=True,
        blank=True,
        )
    description = models.TextField()
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        """ Change verbose name and ordering in admin """
        verbose_name_plural = 'Dishes'
        ordering = ['name']


class Wines(models.Model):
    """ Model for wines """
    category = models.ForeignKey(
        'WineCategory',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        )
    name = models.CharField(
        max_length=254,
        unique=True,
        )
    slug_name = models.SlugField(
        max_length=254,
        unique=True,
    )
    image = CloudinaryField(
        'image',
        default='placeholder',
        null=True,
        blank=True,
        )
    description = models.TextField()
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        """ Change verbose name and ordering in admin """
        verbose_name_plural = 'Wines'
        ordering = ['name']