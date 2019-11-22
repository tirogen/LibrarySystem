# Generated by Django 2.2.7 on 2019-11-15 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.CharField(choices=[('Available', 'Available'), ('Rented', 'Rented'), ('Broken', 'Broken'), ('Lost', 'Lost')], default='Available', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='BookTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StartDate', models.DateField()),
                ('EndDate', models.DateField()),
                ('RenewTimes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Isbn',
            fields=[
                ('Isbn', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('Category', models.CharField(choices=[('Fiction', 'Fiction'), ('Business', 'Business'), ('Science', 'Science'), ('None', 'None')], default='None', max_length=20)),
                ('Author', models.CharField(max_length=40)),
                ('Name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('Username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Password', models.CharField(default='123456789', max_length=20)),
                ('Email', models.EmailField(max_length=50)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='F', max_length=20)),
                ('Tel', models.CharField(max_length=10)),
                ('DateOfBirth', models.DateField()),
                ('Address', models.CharField(max_length=50)),
                ('FName', models.CharField(max_length=20)),
                ('LName', models.CharField(max_length=20)),
                ('StartWork', models.DateField()),
                ('Salary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Penalty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Point', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PenaltyTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(auto_now_add=True)),
                ('Time', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TimeIn', models.TimeField(null=True, default=None)),
                ('TimeOut', models.TimeField(null=True, default=None)),
            ],
        ),
        migrations.CreateModel(
            name='RoomTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StartTime', models.TimeField()),
                ('EndTime', models.TimeField()),
                ('Date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('Type', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Password', models.CharField(default='123456789', max_length=20)),
                ('Email', models.EmailField(max_length=50)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Female', max_length=20)),
                ('Tel', models.CharField(max_length=10)),
                ('DateOfBirth', models.DateField()),
                ('Address', models.CharField(max_length=50)),
                ('FName', models.CharField(max_length=20)),
                ('LName', models.CharField(max_length=20)),
                ('Reliable', models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Status', models.CharField(choices=[('Available', 'Available'), ('NotAvailable', 'NotAvailable')], default='Available', max_length=20)),
                ('Librarian', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Librarian')),
            ],
        ),
        migrations.CreateModel(
            name='ReserveFriend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Student')),
                ('Reserve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Reserve')),
            ],
        ),
        migrations.AddField(
            model_name='reserve',
            name='Room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Room'),
        ),
        migrations.AddField(
            model_name='reserve',
            name='RoomTime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.RoomTime'),
        ),
        migrations.AddField(
            model_name='reserve',
            name='Student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Student'),
        ),
        migrations.CreateModel(
            name='Punish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Penalty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Penalty')),
                ('PunishTime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.PenaltyTime')),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Gadget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.CharField(choices=[('Available', 'Available'), ('NotAvailable', 'NotAvailable')], default='Available', max_length=20)),
                ('PurchasedDate', models.DateField()),
                ('Name', models.CharField(max_length=20)),
                ('Room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Room')),
            ],
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Book')),
                ('BookTime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.BookTime')),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Student')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='Isbn',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Isbn'),
        ),
    ]
