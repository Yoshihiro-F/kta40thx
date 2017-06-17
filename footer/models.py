from django.db import models

class Footer(models.Model):
    active_date = models.CharField("活動日時",max_length=30,blank=True)
    active_place = models.CharField("活動場所",max_length=30,blank=True)
    member_numbers = models.IntegerField("会員数", blank=True, help_text="大体でいいです。")
    member_charge = models.CharField("会費",max_length=30, blank=True,help_text="年会費,月会費など")
    address_place = models.TextField("住所", blank=True, max_length=100)
    contact_to = models.CharField("連絡先", blank=True, max_length=30,help_text="もしあれば。")
    mail_address = models.EmailField("メールアドレス", blank=True, help_text="必ず連絡の取れるもので。")


class Related(models.Model):
    footer = models.ForeignKey(Footer, on_delete=models.CASCADE)
    link_name = models.CharField("関連リンク名", max_length=30, blank=True,)
    link_url = models.URLField("URL", max_length=200, blank=True,)
