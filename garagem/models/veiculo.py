from django.db import models

from garagem.models import Marca, Modelo, Categoria, Cor, Acessorio

from uploader.models import Image


class Veiculo(models.Model):
    marca = models.ForeignKey(
        Marca, on_delete=models.PROTECT, related_name="veiculos"
    )
    modelo = models.ForeignKey(
        Modelo, on_delete=models.PROTECT, related_name="veiculos"
        )
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name="veiculos"
    )
    cor = models.ForeignKey(
        Cor, on_delete=models.PROTECT, related_name="veiculos"
    )
    ano = models.IntegerField(null=True,default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=5, null=True, 
    default=0)
    acessorios = models.ManyToManyField(Acessorio, related_name="veiculos")
    foto = models.ManyToManyField(
        Image,
        related_name="+",
        # on_delete=models.CASCADE,
        blank=True,
        default=None,
    )
    
    def __str__(self):
        return f"{self.marca}- {self.modelo}-{self.ano}"
    
    class Meta:
        verbose_name = "veículo"
        verbose_name_plural = "veículos"
