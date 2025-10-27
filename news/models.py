from django.db import models

class Articles(models.Model):
    tittle = models.CharField('Tittle', max_length=50)
    anons = models.CharField('Anons', max_length=250)
    content = models.TextField('Content')
    pub_date = models.DateTimeField('Pub_date')

    def __str__(self):
        return self.tittle

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
