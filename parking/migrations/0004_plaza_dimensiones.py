# Generated by Django 3.2.9 on 2021-12-06 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0003_dimensiones'),
    ]

    operations = [
        migrations.AddField(
            model_name='plaza',
            name='dimensiones',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='parking.dimensiones'),
        ),
    ]