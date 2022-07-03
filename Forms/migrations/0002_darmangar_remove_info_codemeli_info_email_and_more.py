# Generated by Django 4.0.5 on 2022-07-03 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Forms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='darmangar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, null=True, unique=True)),
                ('lname', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('pic', models.ImageField(upload_to='darmanger-image')),
            ],
        ),
        migrations.RemoveField(
            model_name='info',
            name='codemeli',
        ),
        migrations.AddField(
            model_name='info',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='mobile',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='slug',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='info',
            name='talk_about',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='darmanjo_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talk_about', models.TextField()),
                ('rel_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Forms.darmangar')),
            ],
        ),
        migrations.AddField(
            model_name='info',
            name='rel_info',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Forms.darmangar'),
            preserve_default=False,
        ),
    ]
