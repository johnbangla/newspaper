# Generated by Django 3.0.7 on 2020-08-24 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bangla',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, default='title', max_length=4000, null=True)),
                ('papericon', models.ImageField(default='default.jpg', upload_to='photos')),
                ('paperurl', models.CharField(blank=True, default='myurl', max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='English',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, default='title', max_length=4000, null=True)),
                ('papericon', models.ImageField(default='default.jpg', upload_to='photos')),
                ('paperurl', models.CharField(blank=True, default='myurl', max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, default='title', max_length=4000, null=True)),
                ('videoicon', models.ImageField(default='default.jpg', upload_to='photos')),
                ('videourl', models.CharField(blank=True, default='myurl', max_length=400, null=True)),
            ],
        ),
    ]
