from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class HantorismUser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    name = models.CharField(max_length=20)
    student_number = models.CharField(max_length=10)
    major = models.CharField(max_length=20)

    gender = models.CharField(
        max_length=8,
        null=True)
    email = models.CharField(
        max_length=20)
    is_hantor = models.BooleanField()

    objects = models.Manager()


class HantorismPost(models.Model):
    user = models.ForeignKey(HantorismUser, on_delete=models.CASCADE)

    name=models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    view_count = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.title


class HantorismBook(models.Model):
    title = models.CharField(max_length=40)
    state = models.BooleanField(default=False)
    owner = models.CharField(max_length=20)

    def book_return(self):
        self.state = False
        self.save()

    def __str__(self):
        return self.title


class HantorismRentBook(models.Model):
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(HantorismUser, on_delete=models.CASCADE)
    book = models.ForeignKey(HantorismBook, on_delete=models.CASCADE)

    def rent(self):
        self.book.state = True
        self.user = models.ForeignKey(HantorismUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.book.title


