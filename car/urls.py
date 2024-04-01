from django.contrib import admin
from django.urls import include, path
from car import views
from django.conf.urls.static import static
urlpatterns = [ 
path('', views.home, name='home'),
path( 'registered', views.registered, name= 'registered'),
path('login', views.login, name='login'),
path('details', views.details, name='details'),
path('booking', views.booking , name= 'booking'),
path('confirmed', views.confirmed, name='confirmed'),
]
