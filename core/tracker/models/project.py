from django.db import models


class Project(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200, null=False, blank=False)
    start_date = models.DateField(verbose_name='Дата начала', null=True, blank=True)
    end_date = models.DateField(verbose_name='Дата окончания', null=True, blank=True)
    description = models.TextField(verbose_name='Описание', max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
