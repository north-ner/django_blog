# Generated by Django 4.1.7 on 2023-02-21 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='homepage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topNews', models.CharField(max_length=255)),
                ('bottomNews', models.CharField(max_length=255)),
            ],
        ),
    ]
