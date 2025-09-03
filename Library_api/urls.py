from django.urls import path
from .views import BookViewApi,UpdateBookApi,DeleteBookApi,BookSearchPostAPIView,BookCreateApi

urlpatterns = [
    path('book/',BookViewApi.as_view(),name="book view"),
    path('book/create/',BookCreateApi.as_view(), name="book create"),
    # path('book/create/', BookCreate.as_view(), name="book create"),

    path('book/<int:pk>/update/',UpdateBookApi.as_view(), name="book update"),
    path('book/<int:pk>/delete/',DeleteBookApi.as_view(), name="book delete"),
    path('book/search/',BookSearchPostAPIView.as_view(), name="book search"),
]