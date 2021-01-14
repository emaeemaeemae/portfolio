from django.http import HttpResponse
from django.shortcuts import render
from .forms import MebelchelOrdersForm, MebelchelOrdersForm2


def mebelchel(request):
    if request.is_ajax():
        form = MebelchelOrdersForm(request.POST)
        form2 = MebelchelOrdersForm2(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse()

        if form2.is_valid():
            form2.save()
            return HttpResponse()

    form = MebelchelOrdersForm()
    form2 = MebelchelOrdersForm2()

    data = {
        'form': form,
        'form2': form2
    }

    return render(request, 'mebelchel/mebelchel.html', data)
