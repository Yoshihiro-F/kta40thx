"""
WSGI config for kta40thx project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

# -*- coding: utf-8 -*-

import os, sys ,site

sys.path.append('/home/yoshihiro/.pyenv/kta40thx/lib/python3.5/site-packages')
sys.path.append('/var/www/')
site.addsitedir('/home/yoshihiro/.pyenv/kta40thx/lib/python3.5/site-packages')


from mezzanine.utils.conf import real_project_name
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                  "%s.settings" % real_project_name("kta40thx"))

# PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
# settings_module = "%s.settings" % PROJECT_ROOT.split(os.sep)[-1]
# os.environ["DJANGO_SETTINGS_MODULE"] = settings_module

application = get_wsgi_application()
