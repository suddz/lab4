from django.contrib import admin
from django.urls import path, re_path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.archive, name='archive'),
    re_path(r'^order/(?P<order_id>\d+)$', views.get_order, name='get_order'),
]
