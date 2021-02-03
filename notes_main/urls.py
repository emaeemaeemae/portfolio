from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='notes_main'),
    path('list/', include('notes.urls')),
    path('contacts', views.contacts, name='contacts'),
    path('login', views.UserLoginView.as_view(), name='login'),
    path('register', views.RegisterUserView.as_view(), name='register'),
    path('logout', views.UserLogout.as_view(), name='logout')
]
