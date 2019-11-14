from django.db import models
from rest_framework import serializers


class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'pk')

class Librarian(models.Model):
    Username = models.CharField(max_length=20, primary_key=True)
    Password = models.CharField(max_length=20, default="123456789")
    Email = models.EmailField(max_length=50)
    Gender = models.CharField(max_length=1, choices=[("M","Male"), ("F","Female")], default="F")
    Tel = models.CharField(max_length=10)
    DateOfBirth = models.DateField(auto_now=False, auto_now_add=False)
    Address = models.CharField(max_length=50)
    FName = models.CharField(max_length=20)
    LName = models.CharField(max_length=20)
    StartWork = models.DateField(auto_now=False, auto_now_add=False)
    Salary = models.IntegerField()

class Student(models.Model):
    Username = models.CharField(max_length=20, primary_key=True)
    Password = models.CharField(max_length=20, default="123456789")
    Email = models.EmailField(max_length=50)
    Gender = models.CharField(max_length=1, choices=[("M","Male"), ("F","Female")], default="F")
    Tel = models.CharField(max_length=10)
    DateOfBirth = models.DateField(auto_now=False, auto_now_add=False)
    Address = models.CharField(max_length=50)
    FName = models.CharField(max_length=20)
    LName = models.CharField(max_length=20)
    Reliable = models.IntegerField(default=10)

class Penalty(models.Model):
    PenaltyID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=20)
    Point = models.IntegerField()

class Penalty_Time(models.Model):
    class Meta:
        unique_together = (('Date', 'Time'),)
    Date = models.DateField(primary_key=True, auto_now_add=True)
    Time = models.TimeField(auto_now_add=True)

class Book(models.Model):
    BookID = models.AutoField(primary_key=True)
    Status = models.CharField(max_length=1, choices=[("A","Available"), ("R","Rented")], default="A")
    Category = models.CharField(max_length=3, choices=[("FIC","Fiction"), ("BUS","Business"), ("SC","Science"), ("N/A", "None")], default="N/A")
    Author = models.CharField(max_length=40)
    ISBN = models.CharField(max_length=13)
    Name = models.CharField(max_length=20)

class Book_Time(models.Model):
    class Meta:
        unique_together = (('StartDate', 'EndDate'),)
    StartDate = models.DateField(primary_key=True)
    EndDate = models.DateField()
    RenewTimes = models.IntegerField(default=0)

class Room(models.Model):
    RoomID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=20)
    Capacity = models.IntegerField()
    Type = models.CharField(max_length=1, choices=[("M","MeetingRoom"), ("S","SleepingRoom")], default="M")
    Status = models.CharField(max_length=1, choices=[("A","Available"), ("N","NotAvailable")], default="A")

class Gadget(models.Model):
    GadgetID = models.AutoField(primary_key=True)
    Status = models.CharField(max_length=1, choices=[("A","Available"), ("N","NotAvailable")], default="A")
    PurchasedDate = models.DateField()
    Name = models.CharField(max_length=20)

class Room_Time():
    class Meta:
        unique_together = (('StartTime', 'EndTime', 'Date'),)
    StartTime = models.TimeField()
    EndTime = models.TimeField()
    Date = models.DateField()