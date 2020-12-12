from django.urls import path

from app.views.add_post import add_post
from app.views.delete_post import delete_post
from app.views.details_post import details_post
from app.views.edit_post import edit_post
from app.views.home_page_view import home_page
from app.views.login_and_registration import registration, login_view, logout_view
from app.views.my_posts import my_posts_view
from app.views.pets_filter import pets_filter

urlpatterns = [
    path('', home_page, name='home page'),
    path('pets/<str:version>', pets_filter, name='pets filter'),
    path('register/', registration, name='register page'),
    path('login/', login_view, name='login page'),
    path('logout/', logout_view, name='logout page'),
    path('<str:username>/posts', my_posts_view, name='my posts page'),
    path('add/', add_post, name='add post page'),
    path('details/<int:pk>', details_post, name='details post page'),
    path('edit/<int:pk>', edit_post, name='edit post page'),
    path('delete/<int:pk>', delete_post, name='delete post page')
]
