from django.urls import path
from . import views


urlpatterns = [
   path('',views.homepage, name='homepage'),
   path('requester/',views.requester, name='requester'),
   path('products/',views.products, name='products'),
   path('status/',views.status, name='status'),
   path('register/',views.register, name='register'),
   path('forgot/',views.forgot),
   path('reset/',views.reset),
<<<<<<< HEAD
   path('login/',views.login, name='login'),   
   path('tracker/',views.tracker, name='tracker'),
   path('notif/',views.notification, name='notification'),

] 
=======
   path('login/',views.login, name='login'),
   path('notif/',views.notification, name='notification'),
   path('tracker/',views.tracker, name='tracker'),
   path('verify/',views.verify, name='verify'),
   path('about/',views.about, name='about'),
   path('history/',views.history, name='history'),
]
>>>>>>> ad97589075ca3b4b81fa81a03cb5fdaa1a5cf2f3
