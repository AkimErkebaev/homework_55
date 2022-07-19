from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        abstract = True


class Task(BaseModel):
    name = models.CharField(max_length=50, null=False, blank=False, default="NoName", verbose_name="Название")
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Описание")
    status = models.ForeignKey("webapp.Status", on_delete=models.PROTECT, related_name="statuses",
                               verbose_name='Статус')
    types = models.ManyToManyField("webapp.Type", related_name="tasks", blank=True)

    def __str__(self):
        return f"{self.id}. {self.name} {self.status} {self.types}"

    class Meta:
        db_table = "tasks"
        verbose_name = "Задание"
        verbose_name_plural = "Задания"


class Status(models.Model):
    name = models.TextField(max_length=400, null=False, blank=False, verbose_name='Название')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "statuses"
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"


class Type(models.Model):
    name = models.CharField(max_length=31, verbose_name='Тип')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "types"
        verbose_name = "Тип"
        verbose_name_plural = "Типы"
