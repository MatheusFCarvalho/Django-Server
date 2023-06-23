from django.db import models

class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    client = models.CharField(max_length=100, default='não especificado')
    is_ready = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
