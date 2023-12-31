# Generated by Django 4.0.3 on 2023-05-04 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmsApp', '0005_borrow'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='books',
            name='file_path',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
