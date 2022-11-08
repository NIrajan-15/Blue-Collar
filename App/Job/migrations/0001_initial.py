# Generated by Django 4.0.3 on 2022-11-08 02:11

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(default=None, max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=10)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('created_at', models.DateField()),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Job.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('Part-time', 'Part-time'), ('Full-time', 'Full-time'), ('Contract', 'Contract')], max_length=15)),
                ('street_address', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=30)),
                ('pay_range', models.CharField(max_length=20, null=True)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('employer_name', models.CharField(max_length=30, null=True)),
                ('zip_code', models.IntegerField()),
                ('job_description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('employer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Job.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=20)),
                ('employer', models.CharField(max_length=100)),
                ('start_date', models.CharField(max_length=20)),
                ('end_date', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('Part-time', 'Part-time'), ('Full-time', 'Full-time'), ('Contract', 'Contract')], max_length=20)),
                ('job_description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Job.userprofile')),
            ],
        ),
    ]
