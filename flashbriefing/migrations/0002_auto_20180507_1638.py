# Generated by Django 2.0.5 on 2018-05-07 16:38

from django.db import migrations, models
import flashbriefing.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('flashbriefing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_type',
            field=models.CharField(blank=True, choices=[(flashbriefing.models.ItemType('audio'), 'audio'), (flashbriefing.models.ItemType('text'), 'text')], max_length=16),
        ),
        migrations.AlterField(
            model_name='item',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
