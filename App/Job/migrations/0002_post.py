# Generated by Django 4.0.3 on 2022-10-02 00:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('created_at', models.DateField(default=datetime.datetime(2022, 10, 1, 19, 32, 17, 973090))),
                ('user_porfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Job.userprofile')),
            ],
        ),
    ]
