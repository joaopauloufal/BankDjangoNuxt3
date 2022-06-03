from rest_framework import serializers
from .models import Bank, Agency, Client, Account


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['id', 'bank_code', 'name']


class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = ['id', 'name', 'agency_code', 'bank']
        depth = 1

    def __init__(self, *args, **kwargs):
        super(AgencySerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and (request.method == 'POST' or request.method == 'PUT'):
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'cpf_cnpj']


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['id', 'number', 'type', 'client', 'balance', 'agency']


class AccountBankDepositSerializer(serializers.Serializer):
    value = serializers.DecimalField(max_digits=19, decimal_places=2, required=True, min_value=0.01)


class AccountWithdrawSerializer(serializers.Serializer):
    value = serializers.DecimalField(max_digits=19, decimal_places=2, required=True, min_value=0.01)
