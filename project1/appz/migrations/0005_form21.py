# Generated by Django 5.0.4 on 2024-04-29 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appz', '0004_formpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='form21',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=150)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
