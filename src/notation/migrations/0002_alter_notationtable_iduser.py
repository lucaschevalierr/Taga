# Generated by Django 4.0.1 on 2022-01-21 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_id'),
        ('notation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notationtable',
            name='idUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='user.user'),
        ),
    ]
