from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


STATE_CHOICE = (('Able', 'able'), ('Wait', 'wait'), ('Unable', 'unable'))


class HantorismUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

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
    user_info = models.ForeignKey(HantorismUser, on_delete=models.CASCADE)

    name = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    view_count = models.IntegerField(null=True, default=0)
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class HantorismPostComment(models.Model):
    user_info = models.ForeignKey(HantorismUser, on_delete=models.CASCADE)
    post = models.ForeignKey(HantorismPost, on_delete=models.CASCADE)
    context = models.CharField(max_length=200)


class HantorismBook(models.Model):
    title = models.CharField(max_length=40)
    state = models.CharField(default='able', max_length=40, choices=STATE_CHOICE)
    owner = models.CharField(max_length=20)

    def book_return(self):
        self.state = False
        self.state = 'Wait'
        self.save()

    def __str__(self):
        return self.title


class HantorismRentBook(models.Model):
    date = models.DateTimeField(default=timezone.now)
    user_info = models.ForeignKey(HantorismUser, on_delete=models.CASCADE)
    book = models.ForeignKey(HantorismBook, on_delete=models.CASCADE)

    def rent(self):
        self.book.state = 'Wait'
        self.user_info = models.ForeignKey(HantorismUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.book.title


