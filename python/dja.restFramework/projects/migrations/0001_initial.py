# Generated by Django 4.2.4 on 2023-08-05 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('technology', models.CharField(max_length=200)),
            ],
        ),
    ]