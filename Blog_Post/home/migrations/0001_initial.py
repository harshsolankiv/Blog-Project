# Generated by Django 3.0.5 on 2022-02-20 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('content', models.TextField()),
            ],
        ),
    ]
