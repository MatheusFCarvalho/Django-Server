from django.db import models
from myuser.models import User
from datetime import date, datetime

DESTINY_FIELDS = (
    ('retira', 'Retira'),
    ('entrega', 'Entrega'),
    ('retira-entrega', 'Retira-Entrega'),
)

class CustomDateField(models.DateField):
    def to_python(self, value):
        if isinstance(value, str):
            try:
                return datetime.strptime(
    date,value, '%d/%m/%Y').date()
            except ValueError:
                raise ValueError('Invalid date format. Use the format DD/MM/YYYY.')
        return super().to_python(value)

class Order(models.Model):
    id = models.IntegerField(primary_key=True)
    client = models.CharField(max_length=100, default='não especificado')
    seller = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_billing = CustomDateField()
    is_ready = models.BooleanField(default=False)
    destiny = models.CharField(max_length=15, choices=DESTINY_FIELDS, default='retira')
    estage = models.CharField(default='Produção')
    

    def data_faturamento(self):
        return self.data.strftime('%d/%m/%Y')

    def __str__(self):
        return str(self.id)

    def calculate_color(self):
        if not self.is_ready:
            return 'light-yellow'
        elif self.estage in ['RETIRADO', 'ENTREGUE']:
            return 'light-purple'
        else:
            return 'light-green'
