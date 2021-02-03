from django.urls import path
from . import views

urlpatterns = [
    path('', views.NotesListView.as_view(), name='notes_home'),
    path('create', views.create, name='create'),
    path('<note_id_url>', views.NoteDetailView.as_view(), name='note-detail'),
    path('<note_id_url>/update', views.NoteUpdateView.as_view(), name='note-update'),
    path('<note_id_url>/delete', views.NoteDeleteView.as_view(), name='note-delete')
]
