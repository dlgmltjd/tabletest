# Generated by Django 4.2.1 on 2023-05-31 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tabletest", "0002_department_delete_mymodel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="department",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
