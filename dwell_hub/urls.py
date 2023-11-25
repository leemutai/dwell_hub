"""
URL configuration for dwell_hub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from main_app import views

urlpatterns = [
    path('', views.home, name="home"),
    path('user', views.all_users, name="all"),
    path('user/<int:user_id>', views.user_details, name="details"),
    path('user', views.user, name="user"),


    path('property', views.property, name="property"),
    path('review', views.review, name="review"),
    path('message', views.message, name="message"),
    path('appointment', views.appointment, name="appointment"),
    path('payment', views.payment, name="payment"),

    path('properties', views.properties, name="properties"),
    path('property_details', views.property_details, name="property_details"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
