# Generated by Django 4.1.7 on 2023-04-26 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0007_derniereligne_delete_lastrow'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeartRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('bpm', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='derniereligne',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
