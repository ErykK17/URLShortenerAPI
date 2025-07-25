from django.db import models

class ShortURL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(
        max_length=10,
        unique=True
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.short_url}"