# Generated by Django 4.0.2 on 2022-03-28 19:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0010_reviewer_nonreviewer_helpingstaff'),
        ('Complaint', '0002_complaints_delete_createcomplaint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='reviewer',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='Authentication.reviewer'),
            preserve_default=False,
        ),
    ]
