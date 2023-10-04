from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
  

def homepage(request):
    return render(request, 'accounts/User/homepage.html')


def register(request):
    if request.method == "POST":
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
        messages.success(request, "Your account is successfully created.")
        
        return redirect('login')
    return render(request, 'accounts/User/register.html')


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

def pro_file(request):
    return render(request, 'accounts/User/pro_file.html')

def profile(request):
    return render(request, 'accounts/User/profile.html')

def profile_html(request):
    return render(request, 'profile.html')

def notification_html(request):
    return render(request, 'notification.html')

def pro_file_html(request):
    return render(request, 'pro_file.html')

def signout(request):
    pass

def about_cash(request):
    return render(request, 'accounts/Admin/Accounting/about_cash.html')

def cash_disbursement(request):
    return render(request, 'accounts/Admin/Accounting/cash_disbursement.html')

def home_cash(request):
    return render(request, 'accounts/Admin/Accounting/home_cash.html')

def prequest(request):
    return render(request, 'accounts/Admin/Accounting/prequest.html')

def form(request):
    return render(request, 'accounts/Admin/Accounting/form.html')

def decline(request):
    return render(request, 'accounts/Admin/Accounting/decline.html')

def notice_of_reward(request):
    return render(request, 'accounts/Admin/Accounting/notice_of_reward.html')

def prequest(request):
    return render(request, 'accounts/Admin/Accounting/prequest.html')


def campus_director_requester(request):
    return render(request, 'accounts/Admin/campusD/requester.html')

def campus_director_notification(request):
    return render(request, 'accounts/Admin/campusD/notification.html')

def campus_director_resolution(request):
    return render(request, 'accounts/Admin/campusD/resolution.html')

def campus_director_historycd(request):
    return render(request, 'accounts/Admin/campusD/historycd.html')

def campus_director_about(request):
    return render(request, 'accounts/Admin/campusD/about.html')

def supply_office_home(request):
    return render(request, 'accounts/Admin/Supply_office/home.html')


def home(request):
    return render(request, 'accounts/Accounting/home.html')


def signout(request):
    pass
def supply_office_notification(request):
    return render(request, 'accounts/Admin/Supply_office/notification.html')

def supply_office_history(request):
    return render(request, 'accounts/Admin/Supply_office/history.html')

def supply_office_about(request):
    return render(request, 'accounts/Admin/Supply_office/about.html')

def supply_office_inventory(request):
    return render(request, 'accounts/Admin/Supply_office/inventory.html')

def notice_of_reward(request):
    return render(request, 'accounts/Admin/Accounting/notice_of_reward.html')

def bac(request):
    return render(request, 'accounts/Admin/BAC/bac.html')


department_mapping = {
    'option1': 'College of Arts and Sciences',
    'option2': 'College of Agriculture',
    'option3': 'College of Forestry',
    'option4': 'College of Hospitality Management and Tourism',
    'option5': 'College of Technology and Engineering',
    'option6': 'College of Education',
    'option7': 'Graduate School',
}


def requester(request):
    
    if request.method == "POST":
        

        name = request.POST.get('item_name[]', '')
        description = request.POST.get('item_description[]', '')
        quantity = int(request.POST.get('quantity[]', 0))
        unit_price = float(request.POST.get('unit_price[]', 0))
        purpose= request.POST.get('item_purpose', '')
        department_option = request.POST.get('departmentDropdown', '')  # Get the selected department option

        # Map the selected option to the department name
        department_name = department_mapping.get(department_option, '')

        purpose = request.POST.get('item_purpose', '')
        
        # Assuming you have a logged-in user
        user = request.user

        print('ganagana')

        # Create and save the item
        item = Item(user=user, name=name, description=description, quantity=quantity, unit_price=unit_price, department=department_name, purpose=purpose)
        item.save()
        print('ganahin')
        
        messages.success(request, "Item added successfully.")
        
        return redirect('requester')  # Redirect to the same page after submission
    return render(request, 'accounts/User/requester.html')


