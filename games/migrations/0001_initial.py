# Generated by Django 2.0.5 on 2018-05-04 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('name', models.CharField(blank=True, default='', max_length=200)),
                ('release_date', models.DateTimeField()),
                ('game_category', models.CharField(blank=True, default='', max_length=200)),
                ('played', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
