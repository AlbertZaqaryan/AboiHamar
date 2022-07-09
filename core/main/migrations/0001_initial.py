# Generated by Django 4.0.6 on 2022-07-09 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nout name')),
                ('price', models.IntegerField(verbose_name='Nout price')),
                ('img', models.ImageField(upload_to='media', verbose_name='Nout image')),
            ],
            options={
                'verbose_name': 'Nout',
                'verbose_name_plural': 'Nouts',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Phone name')),
                ('price', models.IntegerField(verbose_name='Phone price')),
                ('img', models.ImageField(upload_to='media', verbose_name='Phone image')),
            ],
            options={
                'verbose_name': 'Phone',
                'verbose_name_plural': 'Phone',
            },
        ),
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Watch name')),
                ('price', models.IntegerField(verbose_name='Watch price')),
                ('img', models.ImageField(upload_to='media', verbose_name='Watch image')),
            ],
            options={
                'verbose_name': 'Watch',
                'verbose_name_plural': 'Watchs',
            },
        ),
    ]
