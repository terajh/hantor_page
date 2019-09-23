from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

STATE_CHOICE = (('Able', 'able'), ('Wait', 'wait'), ('Unable', 'unable'))
MAJOR_CHOICE = (('소프트웨어학과', '소웨'),
                ('사이버보안학과', '사보'),
                ('미디어학과', '미디어'),
                ('국방디지털융합학과', '국디'),
                ('산업공학과', '산업'))


class HantorismUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    name = models.CharField(max_length=20)
    student_number = models.CharField(max_length=10)
    major = models.CharField(max_length=20)
    score = models.IntegerField(default=0)

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
    up_post = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class HantorismPostComment(models.Model):
    user_info = models.ForeignKey(HantorismUser, on_delete=models.CASCADE)
    post = models.ForeignKey(HantorismPost, on_delete=models.CASCADE)
    context = models.CharField(max_length=200)


class HantorismOverflow(models.Model):
    user_info = models.ForeignKey(HantorismUser, on_delete=models.CASCADE)

    name = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    view_count = models.IntegerField(null=True, default=0)
    state = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class HantorismOverflowAnswer(models.Model):
    user_info = models.ForeignKey(HantorismUser, on_delete=models.CASCADE)
    overflow = models.ForeignKey(HantorismOverflow, on_delete=models.CASCADE)
    body = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    state = models.BooleanField(default=False)


class HantorismOverflowAnswerComment(models.Model):
    user_info = models.ForeignKey(HantorismUser, on_delete=models.CASCADE)
    overflow_answer = models.ForeignKey(HantorismOverflowAnswer, on_delete=models.CASCADE)
    context = models.CharField(max_length=200)


class HantorismBook(models.Model):
    title = models.CharField(max_length=40)
    state = models.CharField(default='able', max_length=40, choices=STATE_CHOICE)
    owner = models.CharField(max_length=20)

    def book_return(self):
        self.state = 'Wait'
        self.save()

    def __str__(self):
        return self.title


class HantorismRentBook(models.Model):
    date = models.DateTimeField(default=timezone.now)
    user_info = models.ForeignKey(HantorismUser, on_delete=models.CASCADE)
    book = models.ForeignKey(HantorismBook, on_delete=models.CASCADE)
    return_request = models.BooleanField(default=False)

    def rent(self):
        self.book.state = 'Wait'
        self.book.save()

    def rent_admin(self):
        self.book.state = 'Unable'
        self.book.save()

    def __str__(self):
        return self.book.title


class HantorismDesk(models.Model):
    name = models.CharField(max_length=20)
    student_number = models.CharField(max_length=9)
    birthday = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=13)
    major = models.CharField(max_length=40, choices=MAJOR_CHOICE)

    def __str__(self):
        return self.student_number
