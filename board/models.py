import datetime

from django.db import models
from django.utils.crypto import get_random_string

class Search(models.Model):
    search = models.TextField(max_length=100)

class Board(models.Model):
    board_title = models.TextField(max_length=100, unique=True)
    sub_id = models.IntegerField(unique=True)
    is_superuser = models.BooleanField()
    board_seq = models.IntegerField()


class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField(max_length=5050)

    create_date = models.DateTimeField(auto_now_add=True)

    name = models.TextField(max_length=100)

    board_choices = (
        ('없음', '없음'),
        ('중요 공지사항', '중요 공지사항'),
        ('공지사항', '공지사항'),
        ('회의록', '회의록'),
        ('회칙', '회칙'),
        ('각종 서식', '각종 서식'),
        ('홍보', '홍보'),
        ('교양분과 활동보고서', '교양분과 활동보고서'),
        ('연대사업분과 활동보고서', '연대사업분과 활동보고서'),
        ('연행예술분과 활동보고서', '연행예술분과 활동보고서'),
        ('종교분과 활동보고서', '종교분과 활동보고서'),
        ('창작분과 활동보고서', '창작분과 활동보고서'),
        ('체육분과 활동보고서', '체육분과 활동보고서'),
        ('학술분과 활동보고서', '학술분과 활동보고서'),

    )

    board = models.CharField(max_length=100, choices=board_choices)

    file1 = models.FileField(null=True, upload_to="", blank=True)

    file2 = models.FileField(null=True, upload_to="", blank=True)

    file3 = models.FileField(null=True, upload_to="", blank=True)

    file4 = models.FileField(null=True, upload_to="", blank=True)

    file5 = models.FileField(null=True, upload_to="", blank=True)
