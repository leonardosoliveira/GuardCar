# Generated by Django 3.1.2 on 2020-12-02 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_estacionamentos_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='estacionamentos',
            name='foto',
            field=models.ImageField(default=models.CharField(max_length=50), upload_to=''),
        ),
    ]
