# Generated by Django 3.2.9 on 2021-11-30 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumesite', '0010_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='bootstrap',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='skills',
            name='css',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='skills',
            name='django',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='skills',
            name='html',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='skills',
            name='js',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='skills',
            name='ps',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='skills',
            name='python',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='skills',
            name='react',
            field=models.IntegerField(),
        ),
    ]