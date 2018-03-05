"""recruitment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from recruitmentprocess.views import index, logout, login, signup,\
    recruiterscreen, aspirantscreen, job_apply, changedrive

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', index),
    url(r'^login/$', login),
    url(r'^signup/$', signup),
    url(r'^logout/$', logout),
    url(r'^recruiterscreen/$', recruiterscreen ),
    url(r'^aspirantscreen/$', aspirantscreen ),
    url(r'^job_apply/([0-9]+)/', job_apply),
    url(r'^changedrive/([0-9]+)/', changedrive),

    

]
