# Generated by Django 4.0.2 on 2022-02-14 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('request_type', models.CharField(max_length=50)),
                ('request_body', models.CharField(max_length=500)),
                ('request_time', models.DateTimeField()),
                ('response', models.CharField(max_length=500)),
                ('response_time', models.DateTimeField()),
            ],
        ),
    ]