from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

GENDER_CHOICES = [
('male','Male'),
('female','Female'),
]
ISHANTOR_CHOICES = [
('hantor','YES'),
('no_hantor','NO'),
]


class HantorismUser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    name = models.CharField(max_length=20)
    studentNum = models.CharField(max_length=10)
    major = models.CharField(max_length=20)

    gender = models.CharField(
        max_length=8,
        choices=GENDER_CHOICES,
        null=True)
    email = models.CharField(
        max_length=20)
    isHantor = models.CharField(
        max_length=10,
        choices=ISHANTOR_CHOICES,
        null=True)
    objects = models.Manager()


class HantorismPost(models.Model):
    userID = models.ForeignKey(HantorismUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title



