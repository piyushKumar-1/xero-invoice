# Generated by Django 3.0.6 on 2020-05-10 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Oauth', '0002_auto_20200510_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='contacts',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='line_items',
        ),
        migrations.RemoveField(
            model_name='lineitems',
            name='tracking',
        ),
        migrations.AddField(
            model_name='contacts',
            name='invoice',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Oauth.Invoice'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lineitems',
            name='invoice',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Oauth.Invoice'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tracking',
            name='lineitems',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Oauth.LineItems'),
            preserve_default=False,
        ),
    ]
