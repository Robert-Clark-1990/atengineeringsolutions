from django.db import models


class Reviews(models.Model):

    class Meta:
        verbose_name_plural = 'Reviews'

    name = models.CharField(max_length=254)
    review = models.TextField()

    def __str__(self):
        return self.name
