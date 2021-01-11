from django.db import models


class CallRequests(models.Model):
    name = models.CharField('Имя', max_length=30)
    phone = models.CharField('Телефон', max_length=16)
    date = models.DateTimeField('Время заявки', auto_now=True)

    def __str__(self):
        return '{:<30} || {: <16} || {: <17}'.format(self.name, self.phone, self.date.strftime('%H:%M, %d/%m/%Y'))

    class Meta:
        verbose_name = 'Заявка на звонок'
        verbose_name_plural = 'Заявки на звонок'

