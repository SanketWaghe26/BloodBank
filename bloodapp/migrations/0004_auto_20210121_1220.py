# Generated by Django 3.1.4 on 2021-01-21 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodapp', '0003_donor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='bloodgroup',
            field=models.CharField(choices=[('AB+', 'AB positive'), ('AB-', 'AB negetive'), ('A+', 'A positive'), ('A-', 'A negetive'), ('B+', 'B positive'), ('B-', 'B negetive'), ('O+', 'O positive'), ('O-', 'O negetive')], max_length=50),
        ),
        migrations.AlterField(
            model_name='donor',
            name='dob',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='donor',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], max_length=70),
        ),
    ]