from django.shortcuts import render, redirect
from .models import Notes
from .forms import NotesForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView


class NotesListView(ListView):
    model = Notes
    template_name = 'notes/notes_home.html'
    context_object_name = 'notes'

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return None

        return Notes.objects.filter(user=self.request.user).order_by('-datetime')


class NoteDetailView(DetailView):
    model = Notes
    template_name = 'notes/details_view.html'
    context_object_name = 'note'
    slug_field = 'note_id'  # поле модели
    slug_url_kwarg = 'note_id_url'  # прописывается в urls

    def get_queryset(self):
        return Notes.objects.filter(user=self.request.user)


class NoteUpdateView(UpdateView):
    model = Notes
    template_name = 'notes/update.html'
    context_object_name = 'note'

    slug_field = 'note_id'
    slug_url_kwarg = 'note_id_url'

    form_class = NotesForm

    def get_queryset(self):
        return Notes.objects.filter(user=self.request.user)


class NoteDeleteView(DeleteView):
    model = Notes
    template_name = 'notes/delete.html'

    slug_field = 'note_id'
    slug_url_kwarg = 'note_id_url'

    success_url = '/notes/'

    def get_queryset(self):
        return Notes.objects.filter(user=self.request.user)


def create(request):
    error = ''
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            form_save = form.save(commit=False)
            form_save.user = request.user
            form_save.save()
            return redirect('notes_home')
        else:
            error = 'Форма заполнена неверно'

    form = NotesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'notes/create.html', data)
