# Generated by Django 5.0 on 2023-12-08 02:37

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Societe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ModelAvion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('melitairie', 'Melitairie'), ('airplane', 'Airplane')], default='airplane', max_length=150)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('typeOfFuel', models.CharField(max_length=150)),
                ('capacityOfFuel', models.PositiveIntegerField()),
                ('Altitude', models.PositiveIntegerField()),
                ('societe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='societe_avion', to='AeroModels.societe')),
            ],
        ),
    ]
