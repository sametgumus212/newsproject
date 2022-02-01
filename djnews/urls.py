"""djnews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import home.home.views
from home.home.views import home_view
from home.home.views import add
from home.home.views import tadd
from home.home.views import btadd
from home.home.views import getcontent
from home.home.views import bingadd
from home.home.views import hoew
from home.home.views import venue_csv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('hoew', hoew, name="hoew"),
    path('add', add, name="add"),
    path('tadd', tadd, name="tadd"),
    path('btadd', btadd, name="btadd"),
    path('bingadd',bingadd,name="bingadd"),
    path('getcontent', getcontent, name="getcontent"),
    path('apps', include('apps.apps.urls')),
    path('home', include('home.home.urls')),
    path('venue_csv', home.home.views.venue_csv, name='venue_csv')

]
