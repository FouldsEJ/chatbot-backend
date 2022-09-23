# Generated by Django 4.1.1 on 2022-09-13 21:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatrooms', '0003_alter_chatroom_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='users',
            field=models.ManyToManyField(related_name='chatrooms_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
