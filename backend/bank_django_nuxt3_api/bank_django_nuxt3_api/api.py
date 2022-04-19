from rest_framework import routers
from bank.api import BankViewSet

router = routers.DefaultRouter()
router.register(r'banks', BankViewSet)
urlpatterns = router.urls
