# Generated by Django 5.0.4 on 2024-04-30 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appz', '0008_form3'),
    ]

    operations = [
        migrations.CreateModel(
            name='modelss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]