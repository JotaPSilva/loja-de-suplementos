# Generated by Django 4.2.6 on 2023-10-16 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Sabor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Produto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
                ("preco", models.DecimalField(decimal_places=2, max_digits=8)),
                ("descricao", models.TextField()),
                ("foto", models.ImageField(upload_to="produtos")),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="gains.categoria",
                    ),
                ),
                (
                    "sabor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="gains.sabor"
                    ),
                ),
            ],
        ),
    ]
