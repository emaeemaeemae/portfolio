from django.shortcuts import render, redirect
from .forms import CallRequestsForm


def index(request):
    if request.method == 'POST':
        form = CallRequestsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = CallRequestsForm()

    data = {
        'form': form
    }

    return render(request, 'index/index.html', data)


def privacy(request):
    return render(request, 'index/privacy.html')
