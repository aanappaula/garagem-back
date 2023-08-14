from django.db import models


class Modelo(models.Model):
    descricao = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.descricao} "

    class Meta:
        verbose_name = "modelo"
        verbose_name_plural = "modelos"
    