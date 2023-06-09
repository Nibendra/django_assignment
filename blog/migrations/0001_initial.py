# Generated by Django 4.2.1 on 2023-05-28 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_name', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('post_image', models.ImageField(upload_to='images')),
                ('post_body', models.TextField(max_length=1000)),
            ],
        ),
    ]
