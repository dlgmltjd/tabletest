# Generated by Django 4.2.1 on 2023-05-31 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tabletest", "0007_alter_department_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="department",
            name="name",
            field=models.CharField(max_length=25),
        ),
    ]
