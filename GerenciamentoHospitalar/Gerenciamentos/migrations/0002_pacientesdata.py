# Generated by Django 2.2.1 on 2019-06-16 21:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gerenciamentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PacientesData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=20)),
                ('sobrenome', models.CharField(max_length=20)),
                ('nasc', models.DateField()),
                ('CPF', models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999)])),
            ],
        ),
    ]