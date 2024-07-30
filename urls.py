"""gasproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from gasapp.views import index,storeUser,Login,about,services,contact,userhome,feedbackform,booking,bookinggasCylinder,uploadkyc,kycUpload,message,orderhistory,payment
urlpatterns = [
    path("admin/", admin.site.urls),
    path("",index,name="index"),
    path("storeUser",storeUser,name="storeUser"),
    path("Login",Login,name="Login"),
    path("about",about,name="about"),
    path("services",services,name="services"),
    path("contact",contact,name="contact"),
    path("userhome",userhome,name="userhome"),
    path("feedbackform",feedbackform,name="feedbackform"),
    path("booking",booking,name="booking"), 
    path("bookinggasCylinder",bookinggasCylinder,name="bookinggasCylinder"),
    path("uploadkyc",uploadkyc,name="uploadkyc"),
    path("kycUpload",kycUpload,name="kycUpload"),
    path("message",message,name="message"),
    path("orderhistory",orderhistory,name="orderhistory"),
    path("payment",payment,name="payment"),
]   