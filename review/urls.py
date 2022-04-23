from django.urls import path

from . import views

app_name = 'review'

urlpatterns = [
    path('write/<int:recipe>', views.write_review, name='write_review'),
]