# Generated by Django 5.0.6 on 2024-06-16 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cultos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('musica_1', models.CharField(blank=True, default='', max_length=50)),
                ('musica_2', models.CharField(blank=True, default='', max_length=50)),
                ('musica_3', models.CharField(blank=True, default='', max_length=50)),
                ('musica_4', models.CharField(blank=True, default='', max_length=50)),
                ('musica_5', models.CharField(blank=True, default='', max_length=50)),
                ('data', models.DateField()),
            ],
        ),
    ]
