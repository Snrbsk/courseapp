# Generated by Django 5.0.6 on 2024-06-19 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]