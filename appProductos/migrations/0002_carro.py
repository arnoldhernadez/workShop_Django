# Generated by Django 4.1.7 on 2023-03-30 01:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appProductos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('valUnit', models.DecimalField(decimal_places=2, max_digits=8)),
                ('estado', models.CharField(choices=[('activo', 'activo'), ('comprado', 'comprado'), ('anulado', 'anulado')], default='activo', max_length=20)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appProductos.producto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
