#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/29 15:09
# @Author  : dk05408
# @Site    : 
# @File    : url.py
# @Software: PyCharm
from django.conf.urls import url,include
from django.contrib import admin
from app2 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^info/', views.info),
    url(r'^home/(\d+)(.*)', views.handle_args),
    url(r'^home/', views.home),
    url(r'^db/add', views.db_add),
    url(r'^db/del', views.db_del),
    url(r'^db/update', views.db_update),
    url(r'^db/select', views.db_select),
    url(r'^db/login', views.db_login),
]