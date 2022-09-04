from django.urls import path
from randomthought import views


app_name = 'thought'

urlpatterns = [
    path('', views.random_thought, name='thought-view'),
    path('<int:pk>', views.detail_thought, name='detail-thought-view'),
    path('update/<int:pk>', views.update_thought, name='update-thought-view'),
    path('delete/<int:pk>', views.delete_thought, name='delete-thought-view'),
    path('create/', views.create_thought, name='create-view'),
    path('create_django/', views.create_thought_django, name="create-django-view"),
    path('api/', views.api, name='api-view'),
    path('view_thoughts/', views.view_thoughts, name='view-thoughts'),
]


