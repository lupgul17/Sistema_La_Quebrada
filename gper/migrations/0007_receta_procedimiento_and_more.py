# Generated by Django 5.0.6 on 2024-10-28 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gper", "0006_tecnicasreceta_detalles"),
    ]

    operations = [
        migrations.AddField(
            model_name="receta",
            name="procedimiento",
            field=models.TextField(default=""),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="receta",
            name="temperaturaServicio",
            field=models.CharField(
                choices=[
                    ("Frio", "Frio"),
                    ("Caliente", "Caliente"),
                    ("Al tiempo", "Al Tiempo"),
                ],
                default="Caliente",
                max_length=10,
            ),
        ),
    ]
