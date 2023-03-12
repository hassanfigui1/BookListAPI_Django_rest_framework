from django.urls import path 
from . import views 
urlpatterns = [
    path('books/', views.ReadOnlyBooks.as_view(
        {
            'get':'list',
            # 'post':'create'
        }
    )),
    path('books/<int:pk>',views.ReadOnlyBooks.as_view({
        'get':'retreive',
    })),
    path('books/<int:pk>',views.Book.as_view({
        'put':'update',
        'patch':'partial_update',
        'delete':'destroy',

    }))
]
