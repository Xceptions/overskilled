# Generated by Django 3.1.3 on 2020-12-01 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OverSkilledApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HowTo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ace_comp', models.TextField()),
                ('ace_comp_res', models.TextField()),
                ('get_proj', models.TextField()),
                ('get_proj_res', models.TextField()),
                ('get_jobs', models.TextField()),
                ('get_jobs_res', models.TextField()),
            ],
        ),
    ]
