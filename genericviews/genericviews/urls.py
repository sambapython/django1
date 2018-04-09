"""genericviews URL Configuration

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
#from app1.views import index
from django.views.generic import TemplateView, ListView, CreateView
from app1.models import Customer
from django.forms import DateInput
from app1.views import CustomerCreateView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', TemplateView.as_view(template_name="app1/index.html")),
    # if you don't mentioned a template_name for list view it will
    # automatically reneder to "appname/modelname_lsit.html: 
    #app1/customer_list.html"
    # queryset=Customer.objects.filter(cust_type="s")
   	url(r'^customer/', ListView.as_view(model=Customer)),
    # redirect to app1/customer_form.html
    url(r'^create_customer/', CustomerCreateView.as_view()),
]



