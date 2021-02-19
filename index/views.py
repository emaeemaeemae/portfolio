from django.http import HttpResponse
from django.shortcuts import render
from .forms import CallRequestsForm
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    if request.is_ajax():
        form = CallRequestsForm(request.POST)

        if form.is_valid():
            send_mail('Заявка на звонок',
                      f"Заявка на звонок от {form['name'].value()}, телефон {form['phone'].value()}",
                      settings.EMAIL_HOST_USER,
                      ['mysin_id@mail.ru'],
                      fail_silently=False)

            form.save()
            return HttpResponse()

    form = CallRequestsForm()

    data = {
        'form': form
    }

    return render(request, 'index/index.html', data)


def privacy(request):
    return render(request, 'index/privacy.html')
