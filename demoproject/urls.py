"""
URL configuration for demoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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


from demoapp1.views import mySquare, voteFromHome, showCurrentDateTime, showDateSpecFormat, showTimeNowAMPMor24HFormat, showTimeAheadorBehind, currentTime
from counter.views import counter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show/<int:side>', mySquare),
    path('vote/<int:age>', voteFromHome),
    path('showDTserver',showCurrentDateTime),
    path("showCurrDate",showDateSpecFormat),
    path('timeAMPM',showTimeNowAMPMor24HFormat),
    path('timeAhedBeh',showTimeAheadorBehind),
    path('time',currentTime),
    path('counter',counter),
    path('', include('newsletterapp.urls')),
    ]
