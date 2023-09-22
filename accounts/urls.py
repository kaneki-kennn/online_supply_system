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
<<<<<<< HEAD
   path('tracker/',views.tracker, name='tracker'),
   path('verify/',views.verify, name='verify'),
   path('about/',views.about, name='about'),
   path('notification/',views.notification, name='notification'),
   path('history/',views.history, name='history'),
=======
   path('notif/',views.notification, name='notification'),

>>>>>>> 0ea241cf795d1b27d6bc8a3490860ba55f0c4889
]