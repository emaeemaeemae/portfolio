from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ShawarmaOrdersForm, ShawarmaOrdersForm2


def shawarma(request):
    if request.is_ajax():
        form = ShawarmaOrdersForm(request.POST)
        form2 = ShawarmaOrdersForm2(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse()

        if form2.is_valid():
            form2.save()
            return HttpResponse()

    form = ShawarmaOrdersForm()
    form2 = ShawarmaOrdersForm2()

    data = {
        'form': form,
        'form2': form2
    }

    return render(request, 'shawarma/shawarma.html', data)
