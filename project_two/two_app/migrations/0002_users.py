# Generated by Django 4.1 on 2023-03-05 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('two_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=256)),
                ('text', models.CharField(max_length=256)),
            ],
        ),
    ]