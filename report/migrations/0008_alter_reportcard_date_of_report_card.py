# Generated by Django 4.2.5 on 2023-09-26 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0007_alter_reportcard_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportcard',
            name='date_of_report_card',
            field=models.DateField(auto_now_add=True),
        ),
    ]
