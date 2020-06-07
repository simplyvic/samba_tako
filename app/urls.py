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
    path('receivemoney/<str:id>/local', views.receivemoney, name="receivemoney"),
	path('confirmation/<str:id>', views.confirmation, name="confirmation"),
    
    path('transferdashboard/', views.transferdashboard, name='transferdashboard'),
    path('pendingmoney/local', views.pendingmoney_local, name='pendingmoney'),
    path('pendingmoney/local/001bakau', views.pendingmoney_local_001bakau, name='pendingmoney_local_001bakau'),
    path('pendingmoney/local/002brusubi', views.pendingmoney_local_002brusubi, name='pendingmoney_local_002brusubi'),
    path('pendingmoney/local/003brufut', views.pendingmoney_local_003brufut, name='pendingmoney_local_003brufut'),
    path('pendingmoney/local/004tallinding', views.pendingmoney_local_004tallinding, name='pendingmoney_local_004tallinding'),
    path('pendingmoney/local/005tippergarrage', views.pendingmoney_local_005tippergarrage, name='pendingmoney_local_005tippergarrage'),
    path('pendingmoney/local/006bansang1', views.pendingmoney_local_006bansang1, name='pendingmoney_local_006bansang1'),
    path('pendingmoney/local/007jangjangbureh', views.pendingmoney_local_007jangjangbureh, name='pendingmoney_local_007jangjangbureh'),
    path('pendingmoney/local/008brikamaba', views.pendingmoney_local_008brikamaba, name='pendingmoney_local_008brikamaba'),
    path('pendingmoney/local/009bansang2', views.pendingmoney_local_009bansang2, name='pendingmoney_local_009bansang2'),
    path('pendingmoney/local/010soma', views.pendingmoney_local_010soma, name='pendingmoney_local_010soma'),
    path('pendingmoney/local/011basse', views.pendingmoney_local_011basse, name='pendingmoney_local_011basse'),
    path('pendingmoney/local/012sinchu', views.pendingmoney_local_012sinchu, name='pendingmoney_local_012sinchu'),


    path('pendingmoney/forex', views.pendingmoney_forex, name='pendingmoney_forex'),
    path('listtransfersall/', views.listtransfersall, name='listtransfersall'),
    path('listtransfersreceived/', views.listtransfersreceived, name='listtransfersreceived'),
    path('settings/', views.settings, name='settings'),
]


# 	url(r'^transferdashboard/$', views.transferdashboard, name='transferdashboard'),
#     url(r'^pendingmoney/$', views.pendingmoney, name='pendingmoney'),
#     url(r'^listtransfersall/$', views.listtransfersall, name='listtransfersall'),
#     url(r'^listtransfersreceived/$', views.listtransfersreceived, name='listtransfersreceived'),
    
