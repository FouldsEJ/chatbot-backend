# Generated by Django 4.1.1 on 2022-09-21 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='sender_id',
            field=models.ForeignKey(blank='True', default=None, on_delete=django.db.models.deletion.CASCADE, related_name='chat_userUSERNAME', to=settings.AUTH_USER_MODEL),
        ),
    ]