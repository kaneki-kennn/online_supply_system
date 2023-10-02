from django.urls import path
from . import views
from .views import get_notifications


urlpatterns = [
   path('',views.homepage, name='homepage'),
   path('requester/',views.requester, name='requester'),
   path('request/',views.request, name='request'),
   path('products/',views.products, name='products'),
   path('status/',views.status, name='status'),
   path('register/',views.register, name='register'),
   path('forgot/',views.forgot, name='forgot'),
   path('reset/',views.reset, name='reset'),
   path('login/',views.login, name='login'),
   path('notification/',views.notification, name='notification'),
   path('tracker/',views.tracker, name='tracker'),
   path('verify/',views.verify, name='verify'),
   path('about/',views.about, name='about'),
   path('history/',views.history, name='history'),
   path('profile/',views.profile, name='profile'),
   path('campus_director/requester/', views.campus_director_requester,name='campusD_requester'),
   path('campus_director/notification/', views.campus_director_notification,name='campusD_notification'),
   path('campus_director/resolution/', views.campus_director_resolution,name='campusD_resolution'),
   path('campus_director/history/', views.campus_director_history,name='campusD_history'),
   path('supply_office/notification/', views.supply_office_notification,name='supply_office_notification'),
   path('supply_office/history/', views.supply_office_history,name='supply_office_history'),
   path('get-notifications/', get_notifications, name='get_notifications'),
   path('api/get-notifications/', views.get_notifications, name='get_notifications'),
]
