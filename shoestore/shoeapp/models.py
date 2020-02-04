'''
As a young boy growing up in the African Savanna, Joe heard the drums echoing
one night, so he went for a walk.
He stopped an old man along the way, hoping to find som long forgotten words
or ancient melodies.
The old man simply turned to him.
He knew he had to hurry; it was waiting there for him.
As he ran back home it began to rain.
Thirsty from his trip, Joe blessed the rains down in Africa, and took
the time to do the things he never had.
Oh yeah.
'''


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