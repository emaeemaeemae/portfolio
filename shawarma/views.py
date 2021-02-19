from django.http import HttpResponse
from django.shortcuts import render
from .forms import ShawarmaOrdersForm, ShawarmaOrdersForm2
from django.core.mail import send_mail
from django.conf import settings


def shawarma(request):
    if request.is_ajax():
        form = ShawarmaOrdersForm(request.POST)
        form2 = ShawarmaOrdersForm2(request.POST)

        if form.is_valid():
            send_mail('Заявка на звонок',
                      f"Заявка на звонок от {form['name'].value()}, телефон {form['phone'].value()}",
                      settings.EMAIL_HOST_USER,
                      ['mysin_id@mail.ru'],
                      fail_silently=False)

            form.save()
            return HttpResponse()

        if form2.is_valid():
            send_mail('Заявка на звонок',
                      f"Заявка на звонок от {form2['name'].value()}, телефон {form2['phone'].value()}",
                      settings.EMAIL_HOST_USER,
                      ['mysin_id@mail.ru'],
                      fail_silently=False)

            form2.save()
            return HttpResponse()

    form = ShawarmaOrdersForm()
    form2 = ShawarmaOrdersForm2()

    data = {
        'form': form,
        'form2': form2
    }

    return render(request, 'shawarma/shawarma.html', data)
