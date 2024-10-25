"""
URL configuration for cpcalendar project.

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
from .views import home, event, event_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.homepage, name='homepage'),
    path('event/', event_list.event_list, name='event_list'),    
    path('event/<int:id>/', event.event_detail, name='event_detail'),
    path('event/new/', event.event_create, name='event_create'),
    path('event/<int:id>/edit/', event.event_edit, name='event_edit'),
    path('event/<int:id>/delete/', event.event_delete, name='event_delete'),
]
