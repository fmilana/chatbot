# Generated by Django 2.0.7 on 2019-07-21 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0010_portfolio_fakechange'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='fakeChange',
            new_name='chatbotChange',
        ),
        migrations.RenameField(
            model_name='portfolio',
            old_name='nextChange',
            new_name='newspostChange',
        ),
        migrations.RemoveField(
            model_name='newspost',
            name='accurate',
        ),
    ]