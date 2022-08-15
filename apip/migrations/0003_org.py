# Generated by Django 4.0.4 on 2022-08-13 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apip', '0002_book_normalize_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Org',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_id', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('rank', models.CharField(max_length=50)),
            ],
        ),
    ]