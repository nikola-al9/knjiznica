# Generated by Django 3.2.9 on 2021-11-10 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('num_pages', models.IntegerField(default=0)),
                ('isbn13', models.CharField(blank=True, max_length=13, null=True)),
            ],
        ),
    ]
