from django.urls import path

from app.views.home_page_view import home_page

urlpatterns = [
    path('', home_page, name='home page')
]
