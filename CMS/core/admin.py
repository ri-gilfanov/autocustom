from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.conf import settings


AdminSite.site_header = 'Панель управления сайтом автомагазина {0}'.format(settings.SITE_NAME)
