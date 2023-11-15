"""mamtaPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  re_path(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  re_path(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  re_path(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import include, re_path
from django.contrib import admin
from django.conf.urls.static import static


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include(("mamtaApp.urls",'mamtaApp'), namespace='mamtaApp')),
    re_path(r'^invoice/', include(("invoice.urls",'invoice'), namespace='invoiceApp')),
    re_path(r'^attendance/', include(("attendance.urls",'attendance'), namespace='attendanceApp')),
    # re_path(r'^api/', include('mamtaApp.api.urls')),
    # re_path(r'^invoiceApi/', include('invoice.api.urls')),
    re_path('', include('pwa.urls'))
]
# handler404 = 'mamtaApp.views.bad_request'
# handler500 = 'mamtaApp.views.bad_server'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)