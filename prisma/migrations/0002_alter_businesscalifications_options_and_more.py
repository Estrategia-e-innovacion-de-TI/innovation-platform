# Generated by Django 4.1 on 2024-07-29 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prisma', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='businesscalifications',
            options={'verbose_name_plural': 'Business Califications'},
        ),
        migrations.AlterModelOptions(
            name='businessvalue',
            options={'verbose_name_plural': 'Business Value'},
        ),
        migrations.AlterModelOptions(
            name='feasibility',
            options={'verbose_name_plural': 'Feasibility'},
        ),
        migrations.AlterModelOptions(
            name='feasibilitycalifications',
            options={'verbose_name_plural': 'Feasibility Califications'},
        ),
        migrations.AlterModelOptions(
            name='usecases',
            options={'verbose_name_plural': 'Use cases'},
        ),
    ]
