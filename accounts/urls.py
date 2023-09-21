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
   path('history/',views.history, name='history'),
=======
   path('about/',views.about, name='about'),
>>>>>>> 380335de494e46d42982c3438089ba3f3a36e36f
]