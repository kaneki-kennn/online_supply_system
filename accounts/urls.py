from django.urls import path
from . import views


urlpatterns = [
   path('',views.homepage),
   path('requester/',views.requester),
   path('products/',views.products),
   path('status/',views.status),
   path('register/',views.register),
   path('login/',views.login, name='login'),
<<<<<<< HEAD
   path('notif/',views.notification, name='notification'),
=======
   path('tracker/',views.tracker, name='tracker'),
>>>>>>> a90c159e000e5ce5a5fa898816c846d9d684a355

]