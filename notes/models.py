from django.db import models
from django.contrib.auth.models import User


class Notes(models.Model):
    note_id = models.PositiveIntegerField('Номер заметки')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=40)
    note = models.TextField('Заметка')
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Заметка пользователя {self.user} № {self.note_id} : {self.title}'

    def get_absolute_url(self):
        return f'/notes/{self.note_id}'

    class Meta:
        unique_together = ('user', 'note_id')
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

    def save(self, *args, **kwargs):
        if not self.note_id:
            self.note_id = (
                                   self.__class__.objects.filter(
                                       user=self.user
                                   ).aggregate(
                                       models.Max('note_id')
                                   )['note_id__max'] or 0
                           ) + 1
        super(Notes, self).save(*args, **kwargs)
