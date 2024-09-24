"""
URL configuration for registrationapp project.

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
from enroll.views import home
from enroll.views import save_data, delete_data, edit_data

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('save/', save_data, name='save'),
    path('delete/', delete_data, name='delete'),
    path('edit/', edit_data, name='edit'),
]
