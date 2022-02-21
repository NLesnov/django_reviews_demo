from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.conf import settings


class Review(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        verbose_name='Автор',
    )
    rating = models.PositiveSmallIntegerField(
        validators=(
            MinValueValidator(1),
            MaxValueValidator(5)
        ),
        verbose_name='Рейтинг',
    )
    comment = models.TextField(
        blank=True,
        default='',
        verbose_name='Текст отзыва',
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания',
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='Отзыв опубликован',
    )

