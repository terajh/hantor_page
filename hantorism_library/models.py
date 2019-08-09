from django.db import models
from django.utils import timezone

# 도서관에서 필요한 모델
#
# book
# -책이름
# -책 소유자
# -대여상태
# -빌린 사람 이름
# -대여 날짜

# userID = models.ForeignKey(HantorismUser, on_delete = models.CASCADE)
from common_hantorism.models import HantorismUser


class Library(models.Model):
    book_name = models.CharField(max_length=20)
    book_rent_state = models.BooleanField(default=False)
    rent_date = models.DateTimeField(default=timezone.now)
    book_user = models.ForeignKey(HantorismUser, on_delete=models.CASCADE)
    book_owner_name = models.CharField(max_length=20)

    def __str__(self):
        return self.book_name

    def rent(self):
        self.book_rent_state = True
        self.book_user = models.ForeignKey(HantorismUser, on_delete=models.CASCADE)