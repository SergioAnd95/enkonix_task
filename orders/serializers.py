from .models import Order

from rest_framework import serializers

from tags.serializers import TagSerializer
from tags.models import Tag


class OrderSerializer(serializers.ModelSerializer):

    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = "__all__"


class OrderSetTagsSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=Tag.objects.all(),
    )

    class Meta:
        model = Order
        fields = ["tags"]

# В наличии модель заказа (упрощенная) и view для их вывода.
# На фронте заказы форматируются
# в канбан доску похожую на trello (в колонки по статусу).
#
# Задача от клиента: добавить функционал тегов как в trello.
# Подробнее (после обсуждения с командой): от бекенда нужно иметь возможность
# 1) Создать тег (id, name, color) / удалить тег / отредактировать тег
# 2) Получить список всех существующих тегов
# 3) Добавить к заказу теги по их id
# (решено передавать с фронта готовый массив
# айдишников тегов вместо add/remove функционала)
# 4) При просмотре заказов видеть список их тегов (в виде полных объектов)
