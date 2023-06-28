from django.db import models
from myuser.models import User
DESTINY_FIELDS = (
    ('retira', 'Retira'),
    ('entrega', 'Entrega'),
    ('retira-entrega', 'Retira-Entrega'),
)

class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    client = models.CharField(max_length=100, default='não especificado')
    seller = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_ready = models.BooleanField(default=False)
    destiny = models.CharField(max_length=15, choices=DESTINY_FIELDS, default='retira')

    def __str__(self):
        return str(self.id)
