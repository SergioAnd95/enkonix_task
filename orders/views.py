from rest_framework import mixins, viewsets

from .serializers import OrderSerializer, OrderSetTagsSerializer
from .models import Order


class OrdersView(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.request.method in ("PUT", "PATCH"):
            return OrderSetTagsSerializer
        return OrderSerializer
