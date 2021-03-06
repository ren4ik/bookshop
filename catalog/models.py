from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Book(models.Model):
    category = models.ForeignKey(
        Category,
        related_name='books',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200, db_index=True)
    year = models.PositiveSmallIntegerField("Дата выпуска книги", null=True)
    author = models.CharField(max_length=200, db_index=True, default="Noname")
    image = models.ImageField(upload_to='books/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', ),)

    def __str__(self):
        return self.name
