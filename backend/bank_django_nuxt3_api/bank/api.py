from rest_framework import viewsets, filters
from .models import Bank
from .serializers import BankSerializer


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['bank_code', 'name']
