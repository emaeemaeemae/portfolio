from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CallRequestsForm
from django.contrib import messages
import json


def index(request):
    # if request.method == 'POST':
    #     form = CallRequestsForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('index')
    if request.is_ajax():
        print('ONE')
        form = CallRequestsForm(request.POST)
        if form.is_valid():
            data = {'message': 'success'}
            print('TWO')
            form.save()
            messages.success(request, 'Profile details updated.')

            return HttpResponse(json.dumps(data), content_type='application/json')

    form = CallRequestsForm()

    data = {
        'form': form
    }

    return render(request, 'index/index.html', data)


def privacy(request):
    return render(request, 'index/privacy.html')
