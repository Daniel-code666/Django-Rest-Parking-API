from django.db import models

# Create your models here.
class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.BooleanField('Estado', default=True)
    created_date = models.DateField('Fecha de creación', auto_now_add=True)
    updated_date = models.DateField('Fecha de actualización', auto_now_add=False)
    deleted_date = models.DateField('Fecha de eliminación', auto_now_add=True)

    class Meta:
        abstract = True
        verbose_name = 'Modelo base'
        verbose_name_plural = 'Modelos base'