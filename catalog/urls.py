from catalog.views import index

from django.urls import path


app_name = 'catalog'
urlpatterns = [
    path('', index, name='index'),
]
