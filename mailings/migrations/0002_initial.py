# Generated by Django 4.2.5 on 2023-10-10 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mailings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mailingsettings',
            name='clients',
            field=models.ManyToManyField(to='mailings.clients', verbose_name='Клиенты'),
        ),
        migrations.AddField(
            model_name='mailingsettings',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailings.messages', verbose_name='Сообщение'),
        ),
        migrations.AddField(
            model_name='mailingsettings',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='log',
            name='mailing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailings.mailingsettings', verbose_name='Рассылка'),
        ),
        migrations.AddField(
            model_name='clients',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
