from django.db import models

# Create your models here.
status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class Task(models.Model):
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Описание")
    status = models.CharField(max_length=50, choices=status_choices, default=status_choices[0][0],
                              verbose_name="Статус")
    done_at = models.DateField(null=True, blank=True, verbose_name="Дата выполнения")

    def __str__(self):
        return f"{self.id}. {self.description}: {self.status}"

    class Meta:
        db_table = "tasks"
        verbose_name = "Задание"
        verbose_name_plural = "Задания"
