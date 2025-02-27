from django.db import models


class Notes(models.Model):
    author_name = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Имя автора')
    header = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(max_length=255, verbose_name='Содержимое')

    def __str__(self):
        return f'{self.header}: {self.content}: {self.author_name}'