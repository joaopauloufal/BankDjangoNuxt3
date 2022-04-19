from rest_framework import serializers
from .models import Bank, Agency, Client, Account


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['id', 'bank_code', 'name']


class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = ['id', 'name', 'bank', 'agency_code']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'cpf_cnpj']


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['id', 'number', 'type', 'client', 'balance', 'agency']


class AcountBankDepositSerializer(serializers.Serializer):
    value = serializers.DecimalField(max_digits=19, decimal_places=2, required=True, min_value=0.01)


class AcountWithdrawSerializer(serializers.Serializer):
    valor = serializers.DecimalField(max_digits=19, decimal_places=2, required=True, min_value=0.01)
