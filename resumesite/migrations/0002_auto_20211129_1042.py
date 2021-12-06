# Generated by Django 3.2.9 on 2021-11-29 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumesite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.TextField(default='hi'),
        ),
        migrations.AddField(
            model_name='post',
            name='message',
            field=models.TextField(default='hi'),
        ),
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.TextField(default='hi'),
        ),
        migrations.AddField(
            model_name='post',
            name='subject',
            field=models.TextField(default='hi'),
        ),
    ]
