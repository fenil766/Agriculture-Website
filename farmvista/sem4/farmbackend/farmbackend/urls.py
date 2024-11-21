"""
URL configuration for farmbackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from farmapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/login/', views.admin_login),
    path('admin/signup/', views.admin_signup),
    path('api/book_appo/', views.book_appo),
    path('api/signup/',views.signup),
    path('api/get-csrf-token/',views.csrf_exempt),
    path('api/del/',views.del_data),
    path('api/login/',views.login),
    path('api/images/',views.up_images),
    path('api/images/get/',views.get_images),
    path('api/show_appo/',views.get_booked_appo),
    path('admin/show_appo/',views.get_booked_appo_admin),
    path('admin/insert_data/',views.soil_test),
    path('api/appointment_details/<str:appo_user>/<str:appo_admin>/<str:appo_date>/', views.get_data_app),
    path('api/crop_disease/', views.upload_crop_photo),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)