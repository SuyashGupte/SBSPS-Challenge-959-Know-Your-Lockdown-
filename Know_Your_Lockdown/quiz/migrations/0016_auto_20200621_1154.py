# Generated by Django 3.0.7 on 2020-06-21 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0015_auto_20200621_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='feelings_due_to_lockdown',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='none', max_length=10),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='therapist',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='none', max_length=10),
        ),
    ]
