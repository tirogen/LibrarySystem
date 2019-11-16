# Generated by Django 2.2.7 on 2019-11-15 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20191115_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='Name',
        ),
        migrations.AddField(
            model_name='isbn',
            name='Name',
            field=models.CharField(default='defaultName', max_length=20),
        ),
        migrations.AlterField(
            model_name='librarian',
            name='Gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=20),
        ),
    ]