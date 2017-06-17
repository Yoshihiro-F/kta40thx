from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import pathlib, os



def index(request):
    set_ing = "/Users/YOSHIHIRO/kta40thx/static/media/uploads/galleries/"
    dir = []
    for path in os.listdir(set_ing):
         dir.append(path)
    return render(request, "../templates/galleries/base_list.html", {'dir':dir})

def detail(request, dirname):
    test = "/Users/YOSHIHIRO/kta40thx/static/media/uploads/galleries/" + dirname + '/'
 #  urls = pathlib.Path(test).resolve() # pathlibモジュールの絶対パス取得コマンド
    fi = []
    for path in os.listdir(test):
        url = "/static/media/uploads/galleries/" + dirname + "/" + path
        fi.append(url)
    try:
        del fi[-1]
    except:
        pass
    return render(request, "../templates/galleries/detail_list.html", {'fi':fi, 'dirname':dirname})

