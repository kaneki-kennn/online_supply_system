from django.urls import path
from . import views


urlpatterns = [
   path('',views.homepage, name='homepage'),
   path('requester/',views.requester),
   path('products/',views.products),
   path('status/',views.status),
   path('register/',views.register, name='register'),
   path('forgot/',views.forgot),
   path('reset/',views.reset),
   path('login/',views.login, name='login'),   
   path('tracker/',views.tracker, name='tracker'),
   path('notif/',views.notification, name='notification'),

] 