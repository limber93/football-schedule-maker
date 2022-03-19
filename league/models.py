from django.db import models


class League(models.Model):
    name = models.CharField('리그 이름', max_length=64)
    country = models.CharField('국가', max_length=64)
    description = models.TextField('리그 설명', max_length=512, blank=True, default='')

    class Meta:
        verbose_name = '축구 리그'
        verbose_name_plural = '축구 리그'
        ordering = ('-name',)

    def __str__(self):
        return f'{self.country}-{self.name}'


class Team(models.Model):
    name = models.CharField('팀 이름', max_length=64)
    league = models.ForeignKey(League, on_delete=models.CASCADE, verbose_name='소속 리그')
    description = models.TextField('팀 설명', max_length=512, blank=True, default='')

    class Meta:
        verbose_name = '축구 팀'
        verbose_name_plural = '축구 팀'
        ordering = ('-name',)

    def __str__(self):
        return f'{self.league}-{self.name}'
