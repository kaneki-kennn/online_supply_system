from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import JsonResponse
from .models import Notification
from django.shortcuts import render
from .forms import ItemForm

# Create your views here.

def home(request):
    requester = Requester.objects.all()
    status = Status.objects.all()
    
    total_requester = requester.count()

    total_status = status.count()
    approved = status.filter(status='Approved').count()
    pending = status.filter(status='Pending').count()
    declined = status.filter(status='Declined').count()

    context = {'requester':requester, 'status': status, 
    'total_requester':  total_requester,
    'total_status': total_status,'approved': approved,
    'pending': pending,'declined': declined}

    return render(request, 'accounts/User/dashboard.html', context)   

def requester(request,):
    requester = Requester.objects.all()
    context= {'requester': requester, 'products': products}
    return render(request, 'accounts/User/requester.html', context)

def products(request):
    products = Products.objects.all()   
    return render(request, 'accounts/User/products.html', {'products': products})

def status(request):
    return render(request, 'accounts/User/status.html') 

def homepage(request):
    return render(request, 'accounts/User/homepage.html')

def register(request):
    if request.method != "POST":
        return render(request, 'accounts/User/register.html')
    username = request.POST['username']
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    contact1 = request.POST['contact1']
    contact2 = request.POST['contact2']
    pass1 = request.POST['pass1']
    pass2 = request.POST['pass2']

    if pass1 != pass2:
        raise ValueError("password not match.")

    myuser = User.objects.create_user(username, email, pass1)
    myuser.first_name = fname
    myuser.last_name = lname

    myuser.save()

    # Display a success message if the user is successfully registered
    messages.success(request, "Your account is successfully created.")

    return redirect('login')


from django.contrib.auth import login as auth_login

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            auth_login(request, user)  # Use auth_login here to avoid conflicts
            fname = user.first_name
            return render(request, "accounts/User/notification.html", {'fname': fname})
        else:
            messages.error(request, "Bad Credentials")
            return redirect('homepage')
    
    return render(request, 'accounts/User/login.html')

def forgot(request):
    return render(request, 'accounts/User/forgot.html')

def reset(request):
    return render(request, 'accounts/User/reset.html')

def verify(request):
    return render(request, 'accounts/User/verify.html')

def about(request):
    return render(request, 'accounts/User/about.html')

def history(request):
    return render(request, 'accounts/User/history.html')

def tracker(request):
    return render(request, 'accounts/User/tracker.html')

def notification(request):
    return render(request, 'accounts/User/notification.html')

def profile(request):
    return render(request, 'accounts/User/profile.html')





def campus_director_requester(request):
    return render(request, 'accounts/Admin/campusD/requester.html')

def campus_director_notification(request):
    return render(request, 'accounts/Admin/campusD/notification.html')

def campus_director_resolution(request):
    return render(request, 'accounts/Admin/campusD/resolution.html')

def campus_director_history(request):
    return render(request, 'accounts/Admin/campusD/history.html')

def supply_office_notification(request):
    return render(request, 'accounts/Admin/Supply_office/notification.html')

def supply_office_history(request):
    return render(request, 'accounts/Admin/Supply_office/history.html')



def create_notification(user, message):
    Notification.objects.create(user=user, message=message)
    
    


def get_notifications(request):
    user = request.user  # Assuming you're using the built-in User model
    notifications = Notification.objects.filter(user=user, is_read=False)
    notifications_data = [{'message': n.message, 'timestamp': n.timestamp} for n in notifications]
    return JsonResponse({'notifications': notifications_data})



def request(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add a success message or redirect to a different page
            return redirect('success_view_name')  # Replace 'success_view_name' with your success view name
    else:
        form = ItemForm()

    return render(request, 'accounts/User/requester.html', {'form': form})
