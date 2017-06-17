from django.db import models


YEAR_CHOICES = (
    ('2016', '2016年度'),
    ('2017', '2017年度'),
    ('2018', '2018年度'),
    ('2019', '2019年度'),
    ('2020', '2020年度'),
    ('2021', '2021年度'),
    ('2022', '2022年度'),
    ('2023', '2023年度'),
    ('2024', '2024年度'),
    ('2025', '2025年度'),
    ('2026', '2026年度'),
    ('2027', '2027年度'),
    ('2028', '2028年度'),
    ('2029', '2029年度'),
    ('2030', '2030年度'),
    ('2031', '2031年度'),
    ('2032', '2032年度'),
    ('2033', '2033年度'),
    ('2034', '2034年度'),
    ('2035', '2035年度'),
    ('2036', '2036年度'),
)

MONTH_CHOICE = (
    ('1', "1月"),
    ('2', "2月"),
    ('3', "3月"),
    ('4', "4月"),
    ('5', "5月"),
    ('6', "6月"),
    ('7', "7月"),
    ('8', "8月"),
    ('9', "9月"),
    ('10', "10月"),
    ('11', "11月"),
    ('12', "12月"),
)


class Planyear(models.Model):
    eve_year =  models.CharField("年度", max_length=5, choices = YEAR_CHOICES, help_text='年度は他と被らないようにしてください。')
    pub_date = models.DateField('作成日', auto_now_add=True)
    up_date = models.DateTimeField('編集日時', auto_now=True)

    def __unicode__(self):
        return self.eve_year


class Planmonth(models.Model):
    planyear = models.ForeignKey(Planyear,  on_delete=models.CASCADE)
    eve_month = models.CharField("月", max_length=3, choices = MONTH_CHOICE, blank=True)
    evently = models.CharField("イベント内容", max_length=50, blank=True)
    description = models.CharField("概要", max_length=80, editable=True, default="複数入力する場合は間を','で区切るように")
    def __unicode__(self):
        return self.eve_month, self.evently