# Generated by Django 2.2.5 on 2019-09-15 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='attractions'),
        ),
    ]
