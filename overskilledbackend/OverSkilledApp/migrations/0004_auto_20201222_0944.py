# Generated by Django 3.1.3 on 2020-12-22 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OverSkilledApp', '0003_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='email',
            field=models.CharField(default='noname@mail.com', max_length=200),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.TextField(default='no message'),
        ),
    ]
