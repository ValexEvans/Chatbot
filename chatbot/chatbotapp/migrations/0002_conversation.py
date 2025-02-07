# Generated by Django 4.2.19 on 2025-02-07 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbotapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messages', models.JSONField(default=list)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
