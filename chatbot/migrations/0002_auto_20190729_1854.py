# Generated by Django 2.2.3 on 2019-07-29 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Message', 'verbose_name_plural': 'Messages'},
        ),
    ]
