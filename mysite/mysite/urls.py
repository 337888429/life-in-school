"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include


from apscheduler.scheduler import Scheduler  
  
from fakedata.views import runall#假设我要执行的函数时app01项目下的views.py中的aaa函数

urlpatterns = [
    path('', include('fakedata.urls')),
    # path('camerainfo/',include('fakedata.urls'))
    path('admin/', admin.site.urls),
]
