# Generated by Django 3.0.6 on 2020-05-11 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Oauth', '0004_auto_20200511_0810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='BrandingThemeID',
        ),
        migrations.RemoveField(
            model_name='lineitems',
            name='LineItemID',
        ),
    ]
