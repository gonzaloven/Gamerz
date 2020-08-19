from django.conf.urls import url

from .views import (
    ProductoListView,
    ProductoDetailSlugView,
)

urlpatterns = [
    url(r'^$', ProductoListView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', ProductoDetailSlugView.as_view())
]