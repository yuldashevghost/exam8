# Generated by Django 5.0.3 on 2024-03-31 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sport", "0002_remove_match_date_delete_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rating",
            name="rating",
            field=models.IntegerField(default=0),
        ),
    ]
