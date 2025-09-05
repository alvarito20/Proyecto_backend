from django.db import models

class Modelo_1(models.Model):
    # Django ya creará 'id' automáticamente
    campo_2_modelo_1 = models.CharField(max_length=200, null=False)
    campo_3_modelo_1 = models.TextField(default='Texto')


class Modelo_2(models.Model):
    # Django ya creará 'id' automáticamente
    campo_2_modelo_2 = models.ForeignKey(Modelo_1, on_delete=models.CASCADE)
    campo_3_modelo_2 = models.DateField()  # max_length eliminado, no aplica
    campo_4_modelo_2 = models.TimeField()
    campo_5_modelo_2 = models.DateTimeField()
    campo_6_modelo_2 = models.IntegerField()
    campo_7_modelo_2 = models.DecimalField(max_digits=10, decimal_places=2)  # Debes definirlos
    campo_8_modelo_2 = models.FloatField()
    campo_9_modelo_2 = models.BooleanField()
    campo_10_modelo_2 = models.EmailField()
    campo_11_modelo_2 = models.URLField()
    campo_12_modelo_2 = models.URLField()
    campo_13_modelo_2 = models.ImageField(upload_to='images/')  # Debes definir ruta
