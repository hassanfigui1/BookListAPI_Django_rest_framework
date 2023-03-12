from django.urls import path 
from . import views 
urlpatterns = [
    path('books/', views.Book.as_view(
        {
            'get':'list',
            'post':'create'
        }
    )),
    path('books/<int:pk>',views.Book.as_view({
        'put':'update',
        'patch':'partial_update',
        'delete':'destroy',
        'get':'retreive'
    }))
]
