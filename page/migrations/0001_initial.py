# Generated by Django 4.1.7 on 2023-03-12 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fomularioModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=23)),
                ('decricao', models.CharField(max_length=166)),
                ('link', models.CharField(max_length=300)),
                ('imagem', models.CharField(max_length=300)),
            ],
        ),
    ]
