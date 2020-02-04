from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=30)
    website = models.URLField()

    def __str__(self):
        return self.name


class ShoeType(models.Model):
    style = models.CharField(max_length=20)

    def __str__(self):
        return self.style


class ShoeColor(models.Model):
    color_name = models.CharField(max_length=20)

    def __str__(self):
        return self.color_name


class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=30)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    material = models.CharField(max_length=30)
    fasten_type = models.CharField(max_length=20)

    def __str__(self):
        return self.brand_name