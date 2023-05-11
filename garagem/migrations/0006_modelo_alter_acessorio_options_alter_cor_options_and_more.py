# Generated by Django 4.1.7 on 2023-05-11 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0005_veiculo_modelo_alter_veiculo_preco'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'modelo',
                'verbose_name_plural': 'modelos',
            },
        ),
        migrations.AlterModelOptions(
            name='acessorio',
            options={'verbose_name': 'acessório', 'verbose_name_plural': 'acessórios'},
        ),
        migrations.AlterModelOptions(
            name='cor',
            options={'verbose_name': 'cor', 'verbose_name_plural': 'cores'},
        ),
        migrations.AlterModelOptions(
            name='veiculo',
            options={'verbose_name': 'veículo', 'verbose_name_plural': 'veículos'},
        ),
    ]