# Generated by Django 3.2.9 on 2021-11-29 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumesite', '0004_alter_post_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='email',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='subject',
            field=models.TextField(),
        ),
    ]