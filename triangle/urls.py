from django.urls import path

from triangle.views import trngl_form


app_name = 'triangle'
urlpatterns = [
    path('', trngl_form, name='triangle-form'),
]
