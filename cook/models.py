from django.conf import settings
from django.db import models
from django.utils import timezone
from django.http import JsonResponse

class Foods(models.Model):
    id = models.CharField(max_length=255, primary_key=True)  # LINEのidを格納するCharFieldを主キーとして設定
    food_name = models.TextField()

    @classmethod
    def save_data(cls, id, food_name):
        obj = cls(id=id, food_name=food_name)
        obj.save()

    @classmethod
    def take_data(cls, id):
        try:
            food = cls.objects.get(id=id)
            data = {'id': food.id, 'food_name': food.food_name}
            return JsonResponse(data)
        except cls.DoesNotExist:
            return JsonResponse({'error': 'Food not found'}, status=404)


