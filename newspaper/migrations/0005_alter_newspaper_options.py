# Generated by Django 4.2.2 on 2023-07-05 11:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("newspaper", "0004_alter_redactor_years_of_experience"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="newspaper",
            options={"ordering": ["published_date"]},
        ),
    ]
