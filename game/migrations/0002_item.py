# Generated by Django 3.2.6 on 2021-08-04 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('cost', models.BigIntegerField()),
                ('description', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.inventory')),
            ],
        ),
    ]