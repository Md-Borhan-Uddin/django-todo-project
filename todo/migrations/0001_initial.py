# Generated by Django 4.2.4 on 2023-08-12 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todoTitle', models.CharField(max_length=255, verbose_name='Title')),
                ('todoDescription', models.TextField(verbose_name='Description')),
                ('is_completed', models.BooleanField(default=False, verbose_name='is Complited')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
