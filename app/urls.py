"""project URL Configuration

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
from django.urls import include, path
from app import views

urlpatterns = [
    # path('', views.transferdashboard, name='transferdashboard'),
    # path('admin/', admin.site.urls),
    # path('accounts/', include('registration.backends.default.urls')),
    path('', views.transferdashboard, name='transferdashboard'),
    path('sendmoney/local', views.sendmoney_local, name='sendmoney_local'),
    path('sendmoney/forex', views.forex, name='forex'),
	path('sendmoney/<str:id>/edit', views.editsendmoney, name="editsendmoney"),
	path('receivemoney/<str:id>/edit', views.receivemoney, name="receivemoney"),
    
    path('transferdashboard/', views.transferdashboard, name='transferdashboard'),
    path('pendingmoney/', views.pendingmoney, name='pendingmoney'),
    path('listtransfersall/', views.listtransfersall, name='listtransfersall'),
    path('listtransfersreceived/', views.listtransfersreceived, name='listtransfersreceived'),
    path('settings/', views.settings, name='settings'),
]


# 	url(r'^transferdashboard/$', views.transferdashboard, name='transferdashboard'),
#     url(r'^pendingmoney/$', views.pendingmoney, name='pendingmoney'),
#     url(r'^listtransfersall/$', views.listtransfersall, name='listtransfersall'),
#     url(r'^listtransfersreceived/$', views.listtransfersreceived, name='listtransfersreceived'),
    
