from rest_framework import viewsets, filters, response, status, serializers
from rest_framework.decorators import action
from .models import Bank, Agency, Account, Client
from .serializers import (
    AccountBankDepositSerializer, AccountWithdrawSerializer, BankSerializer, AgencySerializer, AccountSerializer,
    ClientSerializer
)
from django.db.transaction import atomic
from decimal import Decimal


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['bank_code', 'name']

    @action(detail=True, methods=['get'], serializer_class=AgencySerializer)
    def agencies(self, request, *args, **kwargs):
        bank = self.get_object()
        agencies = self.get_serializer(bank.agencies, many=True)
        return response.Response(agencies.data)


class AgencyViewSet(viewsets.ModelViewSet):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'agency_code']

    @action(detail=True, methods=['get'], serializer_class=AccountSerializer)
    def accounts(self, request, *args, **kwargs):
        agency = self.get_object()
        accounts = self.get_serializer(agency.accounts, many=True)
        return response.Response(accounts.data)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['cpf_cnpj']

    @action(detail=True, methods=['get'], serializer_class=AccountSerializer)
    def accounts(self, request, *args, **kwargs):
        client = self.get_object()
        accounts = self.get_serializer(client.accounts, many=True)
        return response.Response(accounts.data)


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['number', 'client__cpf_cnpj']

    @atomic
    @action(detail=True, methods=['put'], serializer_class=AccountBankDepositSerializer)
    def deposit(self, request, *args, **kwargs):
        account = self.get_object()
        serializer = AccountBankDepositSerializer(data=request.data)
        if serializer.is_valid():
            account.balance += Decimal(serializer.data['value'])
            account.save()
            return response.Response({'message': 'Deposit made successfully!'})
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @atomic
    @action(detail=True, methods=['put'], serializer_class=AccountWithdrawSerializer)
    def withdraw(self, request, *args, **kwargs):
        account = self.get_object()
        serializer = AccountWithdrawSerializer(data=request.data)
        if serializer.is_valid():
            value = Decimal(serializer.data['value'])
            if value > account.balance:
                raise serializers.ValidationError({'value': ['Insufficient balance.']})
            account.balance -= value
            account.save()
            return response.Response({'message': 'Withdraw successful!'})
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
