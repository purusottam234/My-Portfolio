# Generated by Django 3.1 on 2021-06-23 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Facts',
        ),
        migrations.DeleteModel(
            name='Skills',
        ),
        migrations.DeleteModel(
            name='Testimonials',
        ),
    ]
