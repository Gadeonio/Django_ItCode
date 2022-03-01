# Generated by Django 4.0.1 on 2022-03-01 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('pages', models.IntegerField(blank=True, null=True, verbose_name='Количество страниц')),
            ],
        ),
    ]
