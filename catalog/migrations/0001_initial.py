# Generated by Django 2.1.4 on 2018-12-07 18:26

from django.db import migrations
from django.conf import settings

def create_data(apps, schema_editor):
    User = apps.get_model(settings.AUTH_USER_MODEL)
    user = User(pk=1, username="auth0user", is_active=True , email="admin@techiediaries.com")
    user.save()

class Migration(migrations.Migration):
    dependencies = [
    ]
    operations = [
        migrations.RunPython(create_data),
    ]

def jwt_get_username_from_payload_handler(payload):
    return 'auth0user'