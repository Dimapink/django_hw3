from django.db import models


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Phone(BaseModel):
    name = models.CharField(max_length=255)
    price = models.BigIntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=True)
    slug = models.SlugField()

    class Meta:
        indexes = [models.Index(fields=["name", "price", "-price"])]
