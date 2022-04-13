"""temp URL Configuration

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
from django.urls import path
from app import views
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^$', views.SuperAdmin_index, name='SuperAdmin_index'),
    re_path(r'^SuperAdmin_pay_det/$', views.SuperAdmin_pay_det, name='SuperAdmin_pay_det'),
    re_path(r'^SuperAdmin_current_trainees/$', views.SuperAdmin_current_trainees, name='SuperAdmin_current_trainees'),
    re_path(r'^SuperAdmin_current_trainees_payment/$', views.SuperAdmin_current_trainees_payment, name='SuperAdmin_current_trainees_payment'),
    re_path(r'^SuperAdmin_current_trainees_payment_add/$', views.SuperAdmin_current_trainees_payment_add, name='SuperAdmin_current_trainees_payment_add'),
    re_path(r'^SuperAdmin_current_trainees_payment_update/$', views.SuperAdmin_current_trainees_payment_update, name='SuperAdmin_current_trainees_payment_update'),
    re_path(r'^SuperAdmin_previous_trainees_payment/$', views.SuperAdmin_previous_trainees_payment, name='SuperAdmin_previous_trainees_payment'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
