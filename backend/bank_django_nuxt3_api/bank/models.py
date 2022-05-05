from django.db import models


class Bank(models.Model):
    bank_code = models.CharField(verbose_name='Bank Code', max_length=20, unique=True)
    name = models.CharField(verbose_name='Name', max_length=120)

    class Meta:
        ordering = ['bank_code']
        verbose_name = 'Bank'

    def __str__(self):
        return f'{self.bank_code} - {self.name}'


class Agency(models.Model):
    agency_code = models.CharField(verbose_name='Agency Code', max_length=20)
    name = models.CharField(verbose_name='Name', max_length=120)
    bank = models.ForeignKey(Bank, verbose_name='Bank', on_delete=models.PROTECT, related_name='agencies')

    class Meta:
        ordering = ['name']
        verbose_name = 'Agency'
        unique_together = [['agency_code', 'bank']]

    def __str__(self):
        return f'{self.id} - {self.name}'


class Client(models.Model):
    name = models.CharField(verbose_name='Name', max_length=120)
    cpf_cnpj = models.CharField(verbose_name='CPF/CNPJ', max_length=18, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Client'

    def __str__(self):
        return f'{self.cpf_cnpj} - {self.name}'


class Account(models.Model):

    ACCOUNT_TYPES = (
      ('PHYSICAL', 'Physical person'),
      ('LEGAL', 'Legal person'),
    )

    number = models.CharField(verbose_name='Number', max_length=80)
    balance = models.DecimalField(verbose_name='Balance', decimal_places=2, default=0.00, max_digits=19)
    agency = models.ForeignKey(Agency, verbose_name='Agency', on_delete=models.PROTECT, related_name='accounts')
    client = models.ForeignKey(Client, verbose_name='Client', on_delete=models.PROTECT, related_name='accounts')
    type = models.CharField(verbose_name='Type', max_length=15, choices=ACCOUNT_TYPES)

    class Meta:
        ordering = ['number']
        verbose_name = 'Account'
        unique_together = [['client', 'type', 'agency']]

    def __str__(self):
        return f'{self.number} - {self.agency}: {self.client.name} ({self.type})'
