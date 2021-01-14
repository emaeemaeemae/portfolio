from django.http import HttpResponse
from django.shortcuts import render
from .forms import CallRequestsForm


def index(request):
    if request.is_ajax():
        form = CallRequestsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse()

    form = CallRequestsForm()

    data = {
        'form': form
    }

    return render(request, 'index/index.html', data)


def privacy(request):
    return render(request, 'index/privacy.html')
