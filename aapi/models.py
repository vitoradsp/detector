from django.db import models


class Recebedor(models.Model):    
    img = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.img}"

    class Meta:
        verbose_name_plural = "Recebedors"

