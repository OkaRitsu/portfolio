# Generated by Django 3.2.8 on 2021-10-21 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='タイトル')),
                ('content', models.TextField(blank=True, null=True, verbose_name='本文')),
                ('img1', models.ImageField(upload_to='', verbose_name='写真1')),
                ('img2', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真2')),
                ('img3', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真3')),
                ('img4', models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真4')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='作成日')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
            options={
                'verbose_name_plural': 'Product',
            },
        ),
    ]
