# Generated by Django 4.1.1 on 2022-09-15 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0001_initial'),
        ('products_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='useraccount',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, related_name='Product', to='user_auth.useraccount'),
            preserve_default=False,
        ),
    ]
