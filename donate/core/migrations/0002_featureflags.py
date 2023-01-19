# Generated by Django 3.1.14 on 2023-01-18 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_squashed_0015_remove_old_wagtail_localize'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureFlags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enable_upsell_view', models.BooleanField(default=False, help_text='Checking this will allow the upsell view to be displayed after one-time donations', verbose_name='Enable the upsell view')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
