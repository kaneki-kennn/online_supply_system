from django.urls import path
from . import views 


urlpatterns = [
   path('',views.homepage, name='homepage'),
   path('requester/',views.requester, name='requester'),
   path('request/',views.request, name='request'),
   path('register/',views.register, name='register'),
   path('forgot/',views.forgot, name='forgot'),
   path('reset/',views.reset, name='reset'),
   path('login/',views.login, name='login'),
   path('notif/',views.notification, name='notification'),
   path('tracker/',views.tracker, name='tracker'),
   path('verify/',views.verify, name='verify'),
   path('about/',views.about, name='about'),
   path('history/',views.history, name='history'),
   path('profile/',views.profile, name='profile'),
   path('pro_file/',views.pro_file, name='pro_file'),
   path('profile_html/', views.profile_html, name='profile_html'),
   path('notif/', views.notification_html, name='notification_html'),
   path('cash/',views.cash, name='cash'),
   path('home/',views.home, name='home'),
   path('form/',views.form, name='form'),
   path('decline/',views.decline, name='decline'),
   path('prequest/',views.prequest, name='prequest'),
   path('notice_of_reward/',views.notice_of_reward, name='notice_of_reward'),
   path('campus_director/requester/', views.campus_director_requester,name='campusD_requester'),
   path('campus_director/notification/', views.campus_director_notification,name='campusD_notification'),
   path('campus_director/resolution/', views.campus_director_resolution,name='campusD_resolution'),
   path('campus_director/historycd/', views.campus_director_historycd,name='campusD_historycd'),
   path('campus_director/about/', views.campus_director_about,name='campusD_about'),
   path('supply_office/home/', views.supply_office_home,name='supply_office_home'),
   path('supply_office/notification/', views.supply_office_notification,name='supply_office_notification'),
   path('supply_office/history/', views.supply_office_history,name='supply_office_history'),
   path('supply_office/about/', views.supply_office_about,name='supply_office_about'),
   path('supply_office/inventory/', views.supply_office_inventory,name='supply_office_inventory'),
   path('notice_of_reward/',views.notice_of_reward, name='notice_of_reward'),  
]