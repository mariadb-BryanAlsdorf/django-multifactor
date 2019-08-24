# Generated by Django 2.2.3 on 2019-08-17 21:39

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('properties', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('key_type', models.CharField(choices=[('FIDO2', 'FIDO2 Security Device'), ('U2F', 'U2F Security Key'), ('TOTP', 'TOTP Authenticator'), ('Email', 'OTP-over-Email')], max_length=25)),
                ('enabled', models.BooleanField(default=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('expires', models.DateTimeField(blank=True, default=None, null=True)),
                ('last_used', models.DateTimeField(blank=True, default=None, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='multifactor_keys', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]