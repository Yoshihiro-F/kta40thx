from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='static/media/')

class Memberlist(models.Model):
    orderid = models.IntegerField("ID", blank=False, help_text='必須! 1に近いほど上に表示されます。')
    display = models.BooleanField("表示", help_text='✔︎で表示' ,default=True)
    memname = models.CharField("名前",max_length=30, help_text='フルネームでお願いします')
    position = models.CharField("役職",max_length=30)
    itself = models.TextField("自己紹介",max_length=200, help_text='軽く自己紹介 - 学部学科,呼び名,趣味なんでもいいです。')
    image = models.ImageField("画像",upload_to="memberphoto/", storage=fs, blank=True, help_text='画像は任意で')
"""
    # イメージを表示させる関数定義
    def admin_image_view( self):
        return "<img src='%s' style='max-width: 100px; max-height: 100px;'>" % ( self.image.url,)

    admin_image_view.short_description = "画像"
    admin_image_view.allow_tags = True
"""
# http://blog.w32.jp/2013/03/djangoadminimagefield2013-03-12-0947.html
# Djangoつえぇ
# 画像がなぜかアップロードできていないのは、メディアURLでサイトのドメインを指定できていないから
# つまり、サーバーにあげたら動くかもという方向で行く、無理だったら後で変更
