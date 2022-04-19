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
