from django.conf import settings

from django_hosts import patterns, host


host_patterns = patterns('',

    # mysite.local
    host(r'^$',        settings.ROOT_URLCONF, name='www'),

    # blog.mysite.local
    host(r'blog',      'subdomain.urls.blog', name='blog'),

    # api.mysite.local
    host(r'api',       'subdomain.urls.api',  name='api'),
)

