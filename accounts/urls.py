from django.urls import path
from . import views


urlpatterns = [
   path('',views.homepage, name='homepage'),
   path('requester/',views.requester, name='requester'),
   path('products/',views.products, name='products'),
   path('status/',views.status, name='status'),
   path('register/',views.register, name='register'),
<<<<<<< HEAD
   path('forgot/',views.forgot),
   path('reset/',views.reset),
<<<<<<< HEAD
   path('login/',views.login, name='login'),   
   path('tracker/',views.tracker, name='tracker'),
   path('notif/',views.notification, name='notification'),

] 
=======
=======
   path('forgot/',views.forgot, name='forgot'),
   path('reset/',views.reset, name='reset'),
>>>>>>> 3deca9a7107612ab5a799d5469c67bb67da88e5f
   path('login/',views.login, name='login'),
   path('notif/',views.notification, name='notification'),
   path('tracker/',views.tracker, name='tracker'),
   path('verify/',views.verify, name='verify'),
   path('about/',views.about, name='about'),
   path('history/',views.history, name='history'),
<<<<<<< HEAD
]
>>>>>>> ad97589075ca3b4b81fa81a03cb5fdaa1a5cf2f3
=======
    path('profile/',views.profile, name='profile'),
]
>>>>>>> 3deca9a7107612ab5a799d5469c67bb67da88e5f
