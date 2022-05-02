from django.test import TestCase
from .factories import BankFactory, AgencyFactory, ClientFactory, AccountFactory
from rest_framework import status
from .models import Account, Bank, Agency, Client
import factory
import json
from django.forms.models import model_to_dict

CONTENT_TYPE_JSON = 'application/json'


class ApiBankTest(TestCase):

    def test_list(self):
        banks = BankFactory.create_batch(3)
        response = self.client.get('/api/v1/banks/', content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(banks), len(response.data))

    def test_list_bank_agencies(self):
        bank = BankFactory()
        agencies = AgencyFactory.create_batch(3, bank=bank)
        response = self.client.get(f'/api/v1/banks/{bank.id}/agencies/', content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(agencies), len(response.data))

    def test_create(self):
        data = factory.build(dict, FACTORY_CLASS=BankFactory)
        response = self.client.post('/api/v1/banks/', data, content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bank.objects.count(), 1)

    def test_create_error(self):
        data = factory.build(dict, FACTORY_CLASS=BankFactory)
        del data['name']
        response = self.client.post('/api/v1/banks/', data, content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_show(self):
        bank = BankFactory()
        response = self.client.get(f'/api/v1/banks/{bank.id}/', content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update(self):
        bank = BankFactory()
        data = factory.build(dict, FACTORY_CLASS=BankFactory)
        response = self.client.put(f'/api/v1/banks/{bank.id}/', data, content_type=CONTENT_TYPE_JSON)
        bank_updated = Bank.objects.first()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), model_to_dict(bank_updated))

    def test_update_error(self):
        bank = BankFactory()
        data = factory.build(dict, FACTORY_CLASS=BankFactory)
        del data['name']
        response = self.client.put(f'/api/v1/banks/{bank.id}/', data, content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete(self):
        bank = BankFactory()
        response = self.client.get(f'/api/v1/banks/{bank.id}/', content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.delete(f'/api/v1/banks/{bank.id}/')
        response = self.client.get(f'/api/v1/banks/{bank.id}/', content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class AgencyTest(TestCase):

    def test_list(self):
        bank = BankFactory()
        agencies = AgencyFactory.create_batch(3, bank=bank)
        response = self.client.get('/api/v1/agencies/', content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(agencies), len(response.data))

    def test_list_agencies_accounts(self):
        bank = BankFactory()
        agency = AgencyFactory(bank=bank)
        client = ClientFactory()
        AccountFactory(client=client, agency=agency, type='PHYSICAL')
        AccountFactory(client=client, agency=agency, type='LEGAL')
        response = self.client.get(f'/api/v1/agencies/{agency.id}/accounts/', content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(2, len(response.data))

    def test_create(self):
        bank = BankFactory()
        data = factory.build(dict, FACTORY_CLASS=AgencyFactory, bank=bank)
        data['bank'] = bank.id
        response = self.client.post('/api/v1/agencies/', data, content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bank.objects.count(), 1)

    def test_create_error(self):
        bank = BankFactory()
        data = factory.build(dict, FACTORY_CLASS=AgencyFactory, bank=bank, content_type=CONTENT_TYPE_JSON)
        del data['name']
        response = self.client.post('/api/v1/agencies/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_show(self):
        bank = BankFactory()
        agency = AgencyFactory(bank=bank)
        response = self.client.get(f'/api/v1/agencies/{agency.id}/', content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update(self):
        bank = BankFactory()
        agency = AgencyFactory(bank=bank)
        data = factory.build(dict, FACTORY_CLASS=AgencyFactory)
        data['bank'] = bank.id
        response = self.client.put(f'/api/v1/agencies/{agency.id}/', data, content_type=CONTENT_TYPE_JSON)
        agency_updated = Agency.objects.first()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), model_to_dict(agency_updated))

    def test_update_error(self):
        bank = BankFactory()
        agency = AgencyFactory(bank=bank)
        data = factory.build(dict, FACTORY_CLASS=AgencyFactory, bank=bank)
        data['bank'] = bank.id
        del data['name']
        response = self.client.put(f'/api/v1/agencies/{agency.id}/', data, content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete(self):
        bank = BankFactory()
        agency = AgencyFactory(bank=bank)
        response = self.client.get(f'/api/v1/agencies/{agency.id}/', content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.delete(f'/api/v1/agencies/{agency.id}/')
        response = self.client.get(f'/api/v1/agencies/{agency.id}/', content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class ApiClientTest(TestCase):

    def test_list(self):
        clients = ClientFactory.create_batch(3)
        response = self.client.get('/api/v1/clients/', content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(clients), len(response.data))

    def test_create(self):
        data = factory.build(dict, FACTORY_CLASS=ClientFactory)
        response = self.client.post('/api/v1/clients/', data, content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Client.objects.count(), 1)

    def test_list_client_accounts(self):
        bank = BankFactory()
        agency = AgencyFactory(bank=bank)
        client = ClientFactory()
        AccountFactory(client=client, agency=agency, type='PHYSICAL')
        AccountFactory(client=client, agency=agency, type='LEGAL')
        response = self.client.get(f'/api/v1/clients/{client.id}/accounts/', content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(2, len(response.data))

    def test_create_error(self):
        data = factory.build(dict, FACTORY_CLASS=ClientFactory)
        del data['name']
        response = self.client.post('/api/v1/clients/', data, content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_show(self):
        client = ClientFactory()
        response = self.client.get(f'/api/v1/clients/{client.id}/', content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update(self):
        client = ClientFactory()
        data = factory.build(dict, FACTORY_CLASS=ClientFactory)
        response = self.client.put(f'/api/v1/clients/{client.id}/', data, content_type=CONTENT_TYPE_JSON)
        client_updated = Client.objects.first()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), model_to_dict(client_updated))

    def test_update_error(self):
        client = ClientFactory()
        data = factory.build(dict, FACTORY_CLASS=ClientFactory)
        del data['name']
        response = self.client.put(f'/api/v1/clients/{client.id}/', data, content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete(self):
        client = ClientFactory()
        response = self.client.get(f'/api/v1/clients/{client.id}/', content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.delete(f'/api/v1/clients/{client.id}/')
        response = self.client.get(f'/api/v1/clients/{client.id}/', content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class ApiAccountTest(TestCase):

    def setUp(self):
        self.bank = BankFactory()
        self.agency = AgencyFactory(bank=self.bank)
        self.client_agency = ClientFactory()

    def test_list(self):
        accounts = AccountFactory.create_batch(3)
        response = self.client.get('/api/v1/accounts/', content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(accounts), len(response.data))

    def test_create(self):
        data = factory.build(dict, FACTORY_CLASS=AccountFactory, client=self.client_agency, agency=self.agency)
        data['client'] = self.client_agency.id
        data['agency'] = self.agency.id
        response = self.client.post('/api/v1/accounts/', data, content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Account.objects.count(), 1)

    def test_create_error(self):
        data = factory.build(dict, FACTORY_CLASS=AccountFactory, client=self.client_agency, agency=self.agency)
        data['client'] = self.client_agency.id
        data['agency'] = self.agency.id
        del data['agency']
        response = self.client.post('/api/v1/accounts/', data, content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_show(self):
        account = AccountFactory()
        response = self.client.get(f'/api/v1/accounts/{account.id}/', content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update(self):
        conta = AccountFactory()
        data = factory.build(dict, FACTORY_CLASS=AccountFactory, client=self.client_agency, agency=self.agency)
        data['client'] = self.client_agency.id
        data['agency'] = self.agency.id
        response = self.client.put(f'/api/v1/accounts/{conta.id}/', data, content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_error(self):
        account = AccountFactory()
        data = factory.build(dict, FACTORY_CLASS=AccountFactory, client=self.client_agency, agency=self.agency)
        data['client'] = self.client_agency.id
        del data['agency']
        response = self.client.put(f'/api/v1/accounts/{account.id}/', data, content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete(self):
        account = AccountFactory()
        response = self.client.get(f'/api/v1/accounts/{account.id}/', content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.delete(f'/api/v1/accounts/{account.id}/')
        response = self.client.get(f'/api/v1/accounts/{account.id}/', content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_insert_accounts_same_agency_type_error(self):
        data = factory.build(dict, FACTORY_CLASS=AccountFactory, client=self.client_agency, agency=self.agency, tipo='PHYSICAL')
        data['client'] = self.client_agency.id
        data['agency'] = self.agency.id
        response = self.client.post('/api/v1/accounts/', data, content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post('/api/v1/accounts/', data, content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_withdraw_success(self):
        account = AccountFactory(client=self.client_agency, agency=self.agency, balance=80.00)
        data = {
            'value': 50.00
        }
        response = self.client.put(f'/api/v1/accounts/{account.id}/withdraw/', data, content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        message = {'message': 'Withdraw successful!'}
        self.assertEqual(message, response.data)

        account = Account.objects.first()
        self.assertEqual(account.balance, 30.00)

    def test_value_less_than_balance(self):
        account = AccountFactory(client=self.client_agency, agency=self.agency, balance=80.00)
        data = {
            'value': 90.00
        }
        response = self.client.put(f'/api/v1/accounts/{account.id}/withdraw/', data, content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        message = 'Insufficient balance.'
        self.assertEqual(message, response.data['value'][0])

    def test_withdraw_negative_value(self):
        account = AccountFactory(client=self.client_agency, agency=self.agency, balance=80.00)
        data = {
            'value': -5.00
        }
        response = self.client.put(f'/api/v1/accounts/{account.id}/withdraw/', data, content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_withdraw_zero_value(self):
        account = AccountFactory(client=self.client_agency, agency=self.agency, balance=80.00)
        data = {
            'value': 0.00
        }
        response = self.client.put(f'/api/v1/accounts/{account.id}/withdraw/', data, content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_deposit_success(self):
        account = AccountFactory(client=self.client_agency, agency=self.agency, balance=80.00)
        data = {
            'value': 50.00
        }
        response = self.client.put(f'/api/v1/accounts/{account.id}/deposit/', data, content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        message = {'message': 'Deposit made successfully!'}
        self.assertEqual(message, response.data)

        account = Account.objects.first()
        self.assertEqual(account.balance, 130.00)

    def test_deposit_negative_value(self):
        account = AccountFactory(client=self.client_agency, agency=self.agency, balance=80.00)
        data = {
            'value': -5.00
        }
        response = self.client.put(f'/api/v1/accounts/{account.id}/deposit/', data, content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_deposit_zero_value(self):
        account = AccountFactory(client=self.client_agency, agency=self.agency, balance=80.00)
        data = {
            'value': 0.00
        }
        response = self.client.put(f'/api/v1/accounts/{account.id}/deposit/', data, content_type=CONTENT_TYPE_JSON)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
