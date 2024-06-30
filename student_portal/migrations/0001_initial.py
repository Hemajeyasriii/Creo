# Generated by Django 5.0.6 on 2024-06-27 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Age', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('city', models.TextField(null=True)),
            ],
        ),
    ]
