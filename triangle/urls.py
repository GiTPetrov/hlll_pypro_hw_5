from django.urls import path

from triangle.views import index, person_form, person_list, person_update_form, trngl_form


app_name = 'triangle'
urlpatterns = [
    path('', index, name='index'),
    path('person/', person_form, name='person-form'),
    path('personlist/', person_list, name='person-list'),
    path('person/<int:pk>/', person_update_form, name='person-update-form'),
    path('triangle/', trngl_form, name='triangle-form'),
]
