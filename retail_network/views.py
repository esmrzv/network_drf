from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from retail_network.models import Network, Product
from retail_network.serializers import NetworkSerializer, ProductSerializer
from users.permissions import IsActiveUser


# Create your views here.

class NetworkViewSet(viewsets.ModelViewSet):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = [IsActiveUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']

    def perform_update(self, serializer):
        if "debt_to_supplier" in serializer.validated_data:
            serializer.validated_data.pop("debt_to_supplier")
            raise Exception("Вы не можете менять поле задолженности")
        super().perform_update(serializer)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveUser]
