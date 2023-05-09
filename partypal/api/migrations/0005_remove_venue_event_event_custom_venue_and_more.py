# Generated by Django 4.2 on 2023-05-09 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_event_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venue',
            name='event',
        ),
        migrations.AddField(
            model_name='event',
            name='custom_venue',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='api.venue'),
        ),
    ]