from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=25)
    # store color in hex format
    color = models.CharField(max_length=7)

    def __str__(self):
        return f"{self.name}: {self.color}"
