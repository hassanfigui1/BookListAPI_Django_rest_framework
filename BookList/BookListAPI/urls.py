from django.urls import path 
from . import views 
urlpatterns = [
    path('books/', views.Book.as_view(
        {
            'get':'books',
            'post':'create'
        }
    )),
    path('books/<int: pk>',views.Book.as_view({
        'put':'update',
        'path':'partial_update',
        'delete':'destroy',
        'get':'retrieve'
    }))
]