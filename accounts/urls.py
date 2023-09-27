from django.urls import path
from . import views


urlpatterns = [
   path('',views.homepage, name='homepage'),
   path('requester/',views.requester, name='requester'),
   path('forgot/',views.forgot, name='forgot'),
   path('homepage/',views.homepage, name='homepage'),
   path('login/',views.login, name='login'),
   path('notification/',views.notification, name='notification'),
   path('products/',views.products, name='products'),
   path('register/',views.register, name='register'),
   path('register/',views.register, name='register'),
   path('reset/',views.reset, name='reset'),
   path('status/',views.status, name='status'),
   path('tracker/',views.tracker, name='tracker'),
   path('verify/',views.verify, name='verify'),
   path('profile/',views.profile, name='profile'),
]
   