# Generated by Django 4.1.7 on 2023-03-04 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_soundhomeusersadditionalinfo_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='soundhomeusersadditionalinfo',
            name='avtive',
            field=models.BooleanField(default=False, verbose_name='Status'),
        ),
    ]