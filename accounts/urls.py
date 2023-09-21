from django.urls import path
from . import views


urlpatterns = [
   path('',views.homepage),
   path('requester/',views.requester),
   path('products/',views.products),
   path('status/',views.status),
   path('register/',views.register, name='register'),
   path('forgot/',views.forgot),
   path('login/',views.login, name='login'),
<<<<<<< HEAD
<<<<<<< HEAD
   path('notif/',views.notification, name='notification'),
=======
   path('tracker/',views.tracker, name='tracker'),
>>>>>>> a90c159e000e5ce5a5fa898816c846d9d684a355

=======
>>>>>>> 24240350d1e8efd8c6fa9b52bd4bd2b0d86c1d10
]