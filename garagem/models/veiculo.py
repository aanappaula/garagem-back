from django.db import models

from garagem.models import Marca, Categoria, Cor, Acessorio


class Veiculo(models.Model):
    marca = models.ForeignKey(
        Marca, on_delete=models.PROTECT, related_name="veiculos"
    )
    modelo = models.CharField(max_length=15, null=False, default=0)
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
    
    def __str__(self):
        return f"Marca: {self.marca} Modelo: {self.modelo} Ano: {self.ano} Cor: {self.cor}"
    
    class Meta:
        verbose_name = "veículo"
        verbose_name_plural = "veículos"
