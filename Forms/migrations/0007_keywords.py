# Generated by Django 4.0.5 on 2022-07-03 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forms', '0006_alter_darmanjo_form_information_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='keywords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('darmangar_fi', models.ManyToManyField(to='Forms.darmangar')),
            ],
        ),
    ]
