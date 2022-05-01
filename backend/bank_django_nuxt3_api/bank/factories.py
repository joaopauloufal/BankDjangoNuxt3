import factory
from faker import Faker

from .models import Bank, Agency, Client, Account

faker = Faker()


class BankFactory(factory.django.DjangoModelFactory):
    bank_code = factory.Sequence(lambda n: faker.swift8())
    name = factory.Sequence(lambda n: faker.name())

    class Meta:
        model = Bank


class AgencyFactory(factory.django.DjangoModelFactory):

    name = factory.Sequence(lambda n: faker.name())
    agency_code = factory.Sequence(lambda n: faker.swift8())
    bank = factory.SubFactory(BankFactory)

    class Meta:
        model = Agency


class ClientFactory(factory.django.DjangoModelFactory):

    name = factory.Sequence(lambda n: faker.name())
    cpf_cnpj = factory.Sequence(lambda n: faker.numerify('###.###.###-##'))

    class Meta:
        model = Client

    def physical_client(self):
        self.cpf_cnpj = factory.Sequence(lambda n: faker.numerify('###.###.###-##'))

    def legal_client(self):
        self.cpf_cnpj = factory.Sequence(lambda n: faker.numerify('##.###.###/####-##'))


class AccountFactory(factory.django.DjangoModelFactory):

    number = factory.Sequence(lambda n: faker.swift8())
    balance = factory.Sequence(lambda n: faker.pyfloat(1, 2))
    type = 'PHYSICAL'
    agency = factory.SubFactory(AgencyFactory)
    client = factory.SubFactory(ClientFactory)

    class Meta:
        model = Account

    def physical_account(self):
        self.type = 'PHYSICAL'

    def legal_account(self):
        self.type = 'LEGAL'
