# Generated by Django 5.0.3 on 2024-03-31 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_booking_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
