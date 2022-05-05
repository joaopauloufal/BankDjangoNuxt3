from rest_framework import routers
from bank.api import BankViewSet, AgencyViewSet, AccountViewSet, ClientViewSet

router = routers.DefaultRouter()
router.register(r'banks', BankViewSet)
router.register(r'agencies', AgencyViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'accounts', AccountViewSet)
urlpatterns = router.urls
