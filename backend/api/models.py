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
    Gender = models.CharField(max_length=20, choices=[("Male","Male"), ("Female","Female")], default="Male")
    Tel = models.CharField(max_length=10)
    DateOfBirth = models.DateField(auto_now=False, auto_now_add=False)
    Address = models.CharField(max_length=50)
    FName = models.CharField(max_length=20)
    LName = models.CharField(max_length=20)
    StartWork = models.DateField(auto_now=False, auto_now_add=False)
    Salary = models.IntegerField()

class LibrarianSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Librarian
        fields = ('Username', 'Email', 'Gender', 'Tel', 'DateOfBirth', 'Address', 'FName', 'LName', 'StartWork', 'Salary')

class Student(models.Model):
    Username = models.CharField(max_length=20, primary_key=True)
    Password = models.CharField(max_length=20, default="123456789")
    Email = models.EmailField(max_length=50)
    Gender = models.CharField(max_length=20, choices=[("Male","Male"), ("Female","Female")], default="Female")
    Tel = models.CharField(max_length=10)
    DateOfBirth = models.DateField(auto_now=False, auto_now_add=False)
    Address = models.CharField(max_length=50)
    FName = models.CharField(max_length=20)
    LName = models.CharField(max_length=20)

class Penalty(models.Model):
    Name = models.CharField(max_length=20)
    Point = models.IntegerField()

class PenaltyTime(models.Model):
    Date = models.DateField(auto_now_add=True)
    Time = models.TimeField(auto_now_add=True)

class Isbn(models.Model):
    Isbn = models.CharField(max_length=13, primary_key=True)
    Category = models.CharField(max_length=20, choices=[("Fiction","Fiction"), ("Business","Business"), ("Science","Science"), ("None", "None")], default="None")
    Author = models.CharField(max_length=40)
    Name = models.CharField(max_length=20)

class Book(models.Model):
    Status = models.CharField(max_length=20, choices=[("Available","Available"), ("Rented","Rented"), ("Broken", "Broken"), ("Lost", "Lost")], default="Available")
    Isbn = models.ForeignKey(Isbn, on_delete=models.SET_NULL, null=True)

class BookTime(models.Model):
    StartDate = models.DateField()
    EndDate = models.DateField()
    RenewTimes = models.IntegerField(default=0)

class RoomType(models.Model):
    Type = models.CharField(max_length=20, primary_key=True)
    Capacity = models.IntegerField()

class Room(models.Model):
    Name = models.CharField(max_length=20)
    Status = models.CharField(max_length=20, choices=[("Available","Available"), ("NotAvailable","NotAvailable")], default="Available")
    Librarian = models.ForeignKey(Librarian, on_delete=models.SET_NULL, null=True)
    RoomType = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'Name', 'Status', 'Librarian_id')

class Gadget(models.Model):
    Status = models.CharField(max_length=20, choices=[("Available","Available"), ("NotAvailable","NotAvailable")], default="Available")
    PurchasedDate = models.DateField()
    Name = models.CharField(max_length=20)
    Room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)

class GadgetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gadget
        fields = ('id', 'Status', 'PurchasedDate', 'Name','Room_id')

class RoomTime(models.Model):
    StartTime = models.TimeField()
    EndTime = models.TimeField()
    Date = models.DateField()

class Punish(models.Model):
    Penalty = models.ForeignKey(Penalty, on_delete=models.CASCADE)
    PunishTime = models.ForeignKey(PenaltyTime, on_delete=models.CASCADE)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)

class Borrow(models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Book = models.ForeignKey(Book, on_delete=models.CASCADE)
    BookTime = models.ForeignKey(BookTime, on_delete=models.CASCADE)

class Reserve(models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Room = models.ForeignKey(Room, on_delete=models.CASCADE)
    RoomTime = models.ForeignKey(RoomTime, on_delete=models.CASCADE)
    TimeIn = models.TimeField()
    TimeOut = models.TimeField()

class ReserveSerializer(serializers.HyperlinkedModelSerializer):
    room = RoomSerializer(many=True, read_only=True)
    class Meta:
        model = Reserve
        fields = ('room', 'TimeIn', 'TimeOut')

class ReserveFriend(models.Model):
    Reserve = models.ForeignKey(Reserve, on_delete=models.CASCADE)
    Friend = models.ForeignKey(Student, on_delete=models.CASCADE)
