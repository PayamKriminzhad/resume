# Generated by Django 3.2.9 on 2021-12-14 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumesite', '0003_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='title3',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
