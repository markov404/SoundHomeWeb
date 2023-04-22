# Generated by Django 4.1.7 on 2023-03-07 21:39

from django.db import migrations, models
import users.components.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_soundhomeusers_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soundhomeusers',
            name='email',
            field=models.EmailField(
                max_length=254,
                unique=True,
                validators=[
                    users.components.validators.UserEmailValidator.is_valid]),
        ),
        migrations.AlterField(
            model_name='soundhomeusers',
            name='password',
            field=models.CharField(
                max_length=254,
                validators=[
                    users.components.validators.UserPasswordValidator.is_valid]),
        ),
        migrations.AlterField(
            model_name='soundhomeusersadditionalinfo',
            name='image',
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to='auatars/',
                validators=[
                    users.components.validators.UserAvaValidator.is_valid],
                verbose_name='Auatar'),
        ),
        migrations.AlterField(
            model_name='soundhomeusersadditionalinfo',
            name='nickname',
            field=models.CharField(
                blank=True,
                default='anonim',
                max_length=50,
                null=True,
                unique=True,
                validators=[
                    users.components.validators.UserNicknameValidator.is_valid],
                verbose_name='Name'),
        ),
    ]
