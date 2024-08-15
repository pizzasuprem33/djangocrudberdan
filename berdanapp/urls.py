from django.urls import path
from . import views


urlpatterns = [
    path('genders', views.gender_index),
    path('gender/add', views.gender_create),
    path('gender/store', views.gender_store),
    path('gender/edit/<int:gender_id>', views.gender_edit),
    path('gender/update/<int:gender_id>', views.gender_update),
    path('gender/delete/<int:gender_id>', views.gender_delete),
    path('gender/destroy/<int:gender_id>', views.gender_destroy),

    path('users/', views.user_index, name='user_index'),
    path('user/add', views.user_create),
    path('user/store', views.user_store),
    path('user/edit/<int:user_id>', views.user_edit),
    path('user/update/<int:user_id>', views.user_update),
    path('user/delete/<int:user_id>', views.user_delete),
    path('user/destroy/<int:user_id>', views.user_destroy),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
