from django.db import models

class Cultos(models.Model):
    musica_1 = models.CharField(max_length=50, blank=True, default='')
    musica_2 = models.CharField(max_length=50, blank=True, default='')
    musica_3 = models.CharField(max_length=50, blank=True, default='')
    musica_4 = models.CharField(max_length=50, blank=True, default='')
    musica_5 = models.CharField(max_length=50, blank=True, default='')
    data = models.DateField()
    def __str__(self):
        return f'data: {self.data}'