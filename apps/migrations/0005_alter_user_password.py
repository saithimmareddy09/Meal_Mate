# Generated by Django 4.1.4 on 2023-05-15 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
