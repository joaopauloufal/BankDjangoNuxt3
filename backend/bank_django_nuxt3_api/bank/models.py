from django.db import models


class Bank(models.Model):
    bank_code = models.CharField(verbose_name='Bank Code', max_length=20, unique=True)
    name = models.CharField(verbose_name='Name', max_length=120)

    class Meta:
        ordering = ['bank_code']
        verbose_name = 'Bank'

    def __str__(self):
        return f'{self.bank_code} - {self.name}'
