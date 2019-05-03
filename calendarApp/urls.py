from django.urls import path
from django.conf.urls import include, url
from . import views
from calendarApp import views
from django.contrib.auth import views as auth_views

app_name = 'calendarApp'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register', views.RegisterView, name='register'),
    # The following path was retrieved from:
    #https://stackoverflow.com/questions/4870619/django-after-login-redirect-user-to-his-custom-page-mysite-com-username
    path('account/login/', auth_views.LoginView.as_view),
    path('templates/two_factor/core/login/', auth_views.LoginView.as_view(
        template_name='login.html',
        extra_context={
            'next': '/templates/calendarApp/index.html',
        },
    ), name='login'),

    path('templates/registration/logout.html', views.LogoutView, name='logout'),
    path('index.html', views.IndexView.as_view(), name='index'),
    url(r'^message', views.MessageView.as_view(), name='message'),
    url(r'^calendar', views.event, name='calendar'),
    path('eventNew', views.addEventView, name='new_event'),
    path('event', views.eventView, name='event_view'),
    url(r'^profile', views.ProfileView.as_view(), name='profile'),
]
