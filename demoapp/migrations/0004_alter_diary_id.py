# Generated by Django 4.2.1 on 2023-08-29 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0003_todo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
