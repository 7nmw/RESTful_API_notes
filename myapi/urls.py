from django.urls import path
from . import views
from .views import RegisterView

urlpatterns = [
    path('notes/', views.NotesList.as_view()),
    path('notes/<int:pk>/', views.NotesDetail.as_view()),
    path('register/', RegisterView.as_view(), name='register'),
]
