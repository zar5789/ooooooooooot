# Generated by Django 4.1.1 on 2022-10-26 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=255)),
                ('cat', models.CharField(max_length=255)),
                ('brand_name', models.CharField(max_length=255)),
                ('qty', models.IntegerField()),
                ('price', models.IntegerField()),
                ('picture', models.ImageField(upload_to='')),
            ],
        ),
    ]
