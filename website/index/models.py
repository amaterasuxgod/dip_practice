from django.db import models

class Pc(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(verbose_name='Изображение', default="../static/images/keyboard.png", upload_to="images/")
    processor = models.CharField(max_length=50, default='')
    memory = models.CharField(max_length=50, default='')
    videocard = models.CharField(max_length=50, default='')
    motherboard = models.CharField(max_length=50, default='')
    cores_count = models.CharField(max_length=30, default='')
    core_frequency = models.CharField(max_length=30, default='')
    hard_drive = models.CharField(max_length=100, default='')
    soft_drive = models.CharField(max_length=100, default='')
    price = models.FloatField(max_length=50, default=0.0)

    def __str__(self):
        return self.title