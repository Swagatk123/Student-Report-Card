# Generated by Django 4.2.5 on 2023-09-25 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_alter_subjectmarks_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subjectmarks',
            unique_together=set(),
        ),
    ]