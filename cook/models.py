from django.conf import settings
from django.db import models
from django.utils import timezone


class Foods(models.Model):
    id = models.CharField(max_length=255, primary_key=True)  # LINEのidを格納するCharFieldを主キーとして設定
    info_food = models.TextField()
    condition_food = models.TextField()

    def publish(self):
        pass

    def __str__(self):
        pass


