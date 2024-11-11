from rest_framework.routers import DefaultRouter

from retail_network.apps import RetailNetworkConfig
from retail_network.views import NetworkViewSet, ProductViewSet

app_name = RetailNetworkConfig.name

router = DefaultRouter()
router.register(r'network', NetworkViewSet)
router.register(r'product', ProductViewSet)

urlpatterns = [] + router.urls
