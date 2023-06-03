from django.db import models
from django.contrib.auth.models import User

class Recebedor(models.Model):    
    img = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    def __str__(self):
        return f"{self.img}"

    class Meta:
        verbose_name_plural = "Recebedors"

