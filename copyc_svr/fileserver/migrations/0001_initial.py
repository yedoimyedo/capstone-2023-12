# Generated by Django 4.1.7 on 2023-03-28 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100, unique=True, verbose_name='코드명')),
                ('attached', models.FileField(upload_to='fileserver/', verbose_name='첨부 파일')),
                ('purpose', models.CharField(blank=True, choices=[('FEED', '피드')], default='', max_length=20, verbose_name='용도')),
            ],
        ),
    ]
