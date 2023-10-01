from django.db import models


class TimeValue(models.Model):
    """Таблица time_value, в которой хранятся данные,
       записанные каждые 5* секунд, в формате:
       time : текущая дата/время,
       value : случайное число от 0 до 10"""

    time = models.DateTimeField(primary_key=True)
    value = models.FloatField()

    class Meta:
        managed = False
        db_table = 'time_value'
        ordering = ['-time']


class TimeValueMax(models.Model):
    """Таблица time_value_max, в которой хранятся данные,
       записанные из таблицы time_value,
       если время value больше 9, в формате:
       time : текущая дата/время,
       value : случайное число от 0 до 10"""

    time = models.DateTimeField(primary_key=True)
    value = models.FloatField()

    class Meta:
        managed = False
        db_table = 'time_value_max'
        ordering = ['-time']


class TimeValueAggregated(models.Model):
    """Представление данных таблицы time_value,
       аггрегированные за 1 минуту, в формате:
       minute : время аггрегации,
       avg_value : среднее значение за время"""

    minute = models.DateTimeField(primary_key=True)
    avg_value = models.FloatField()

    class Meta:
        managed = False
        db_table = 'minute_aggregated'
        ordering = ['-minute']
