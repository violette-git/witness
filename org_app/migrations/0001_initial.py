# Generated by Django 4.0.4 on 2022-06-08 04:13

import builtins
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tithe_app', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Orginization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=70)),
                ('website_url', models.URLField(blank=True, null=True)),
                ('facebook_url', models.URLField(blank=True, null=True)),
                ('mission_statement', models.CharField(blank=True, max_length=1000, null=True)),
                ('is_nonprofit', models.BooleanField(default=False, verbose_name='org type')),
                ('members', models.ManyToManyField(related_name='member', to=settings.AUTH_USER_MODEL)),
                ('offering', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offerings', to='tithe_app.offering')),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('goal', models.FloatField(validators=[django.core.validators.MinValueValidator(builtins.min)])),
                ('description', models.CharField(max_length=1000)),
                ('is_complete', models.BooleanField(default=False, verbose_name='goal reached')),
                ('offering', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goals', to='tithe_app.offering')),
            ],
        ),
    ]
