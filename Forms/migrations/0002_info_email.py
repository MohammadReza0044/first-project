# Generated by Django 4.0.5 on 2022-06-19 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
