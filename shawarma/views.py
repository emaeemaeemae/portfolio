from django.shortcuts import render, redirect
from .forms import ShawarmaOrdersForm, ShawarmaOrdersForm2


def shawarma(request):
    if request.method == 'POST':
        form = ShawarmaOrdersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shawarma')

        form = ShawarmaOrdersForm2(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shawarma')

    form = ShawarmaOrdersForm()

    data = {
        'form': form
    }

    return render(request, 'shawarma/shawarma.html', data)
