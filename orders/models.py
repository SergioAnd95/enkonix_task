from django.db import models


class Order(models.Model):
    status = models.CharField(max_length=12)
    tags = models.ManyToManyField("tags.Tag")
