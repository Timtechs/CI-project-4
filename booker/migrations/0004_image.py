# Generated by Django 3.2.16 on 2023-02-13 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booker', '0003_alter_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
