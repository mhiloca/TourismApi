# Generated by Django 2.2.5 on 2019-09-15 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_pontoturistico_mock_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='touristic_places'),
        ),
    ]
