# Generated by Django 3.1.3 on 2020-12-22 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OverSkilledApp', '0004_auto_20201222_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='email',
            field=models.CharField(blank=True, default='noname@mail.com', max_length=200),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.TextField(blank=True, default='no message'),
        ),
    ]
