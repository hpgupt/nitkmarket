# Generated by Django 2.1.2 on 2019-01-12 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(blank=True)),
                ('price', models.TextField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, max_length=5000)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('type', models.TextField(blank=True, max_length=10)),
                ('tag', models.TextField(blank=True, max_length=1000)),
                ('title', models.TextField(blank=True, max_length=1000)),
                ('imagefile', models.FileField(null=True, upload_to='images/', verbose_name='')),
            ],
        ),
    ]