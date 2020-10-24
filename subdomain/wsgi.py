"""
WSGI config for subdomain project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'subdomain.settings')

# application = get_wsgi_application()



activate_this = 'C:/Python37/_apps/django/Pointer2VoidStar/subdomain-demo/venv/Scripts/activate_this.py'
exec(open(activate_this).read(), dict(__file__=activate_this))

import os
import sys
import site

site.addsitedir('C:/Python37/_apps/django/Pointer2VoidStar/subdomain-demo/venv/Lib/site-packages')

sys.path.append('C:/Python37/_apps/django/Pointer2VoidStar/subdomain-demo')
sys.path.append('C:/Python37/_apps/django/Pointer2VoidStar/subdomain-demo/subdomain')

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'subdomain.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'subdomain.settings')

application = get_wsgi_application()
