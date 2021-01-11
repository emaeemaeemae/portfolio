from django.shortcuts import render, redirect
from .forms import MebelchelOrdersForm, MebelchelOrdersForm2


def mebelchel(request):
    if request.method == 'POST':
        form = MebelchelOrdersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mebelchel')

        form = MebelchelOrdersForm2(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mebelchel')

    form = MebelchelOrdersForm()

    data = {
        'form': form
    }

    return render(request, 'mebelchel/mebelchel.html', data)
