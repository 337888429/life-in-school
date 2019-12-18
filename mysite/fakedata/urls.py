from django.urls import path

from . import views



urlpatterns = [

    # path('cid=0/',views.data0, name='data0'),
    # path('cid=1/',views.data1, name='data1'),
    # path('cid=2/',views.data2, name='data2'),
    # path('cid=3/',views.data3, name='data3'),
    path('data',views.data,name='details'),
    path('info',views.info,name='CameraInfo'),
    path('',views.index,name='index')
]
