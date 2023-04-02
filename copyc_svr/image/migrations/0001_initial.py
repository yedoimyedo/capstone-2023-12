# Generated by Django 4.1.7 on 2023-04-02 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='카테고리 명')),
                ('english', models.CharField(max_length=100, verbose_name='영어이름')),
            ],
            options={
                'verbose_name_plural': '카테고리',
            },
        ),
    ]
