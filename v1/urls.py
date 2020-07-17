from django.urls import path

from . import views

urlpatterns = [
    path('<str:shortened>', views.show, name='show')
]
