# Generated by Django 4.0.1 on 2022-01-21 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=100)),
                ('mdp', models.CharField(max_length=100)),
                ('pdb', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
