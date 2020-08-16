"""gamerz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from gamerz.producto.views import (
    ProductoListView,
    producto_list_view,
    ProductoDetailView,
    producto_detail_view,
    ProductoDestacadoListView,
    ProductoDestacadoDetailView
)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^productos/$', ProductoListView.as_view()),
    url(r'^productos-fbv/$', producto_list_view),
    url(r'^productos/(?P<pk>\d+)/$', ProductoDetailView.as_view()),
    url(r'^productos-fbv/(?P<pk>\d+)/$', producto_detail_view),
    url(r'^destacados/$', ProductoDestacadoListView.as_view()),
    url(r'^destacados/(?P<pk>\d+)/$', ProductoDestacadoDetailView.as_view()),
]
