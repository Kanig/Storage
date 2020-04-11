from django.db import models

class landing(models.Model):
	object_name = models.CharField('Наименование', max_length = 50)
	object_value = models.PositiveSmallIntegerField('Количество')
	object_priceBuy = models.PositiveIntegerField('Стоимость Покупки')
	object_priceSell = models.PositiveIntegerField('Стоимость Продажи')
	object_date = models.DateField('Дата')

	def __str__(self):
		return self.object_name

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'


