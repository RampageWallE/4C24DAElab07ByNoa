# Generated by Django 4.2.6 on 2023-10-10 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Evento",
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
                ("nombre", models.CharField(max_length=100)),
                ("lugar", models.CharField(max_length=100)),
                ("fechainicio", models.DateTimeField()),
                ("fechafin", models.DateTimeField()),
                (
                    "fecha_registro",
                    models.DateTimeField(auto_now=True, verbose_name="date published"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Usuario",
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
                ("nombre", models.CharField(max_length=200)),
                ("apellido", models.CharField(max_length=200)),
                ("dni", models.BigIntegerField()),
                ("email", models.EmailField(max_length=254)),
                (
                    "fecha_registro",
                    models.DateTimeField(auto_now=True, verbose_name="date published"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RegistroEvento",
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
                ("cantidad_asientos", models.BigIntegerField()),
                (
                    "fecha_registro",
                    models.DateTimeField(
                        auto_now=True, verbose_name="fecha de registro"
                    ),
                ),
                (
                    "evento",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app1eventos.evento",
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app1eventos.usuario",
                    ),
                ),
            ],
        ),
    ]
