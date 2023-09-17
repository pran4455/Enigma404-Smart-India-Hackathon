from django.shortcuts import render
from django.shortcuts import redirect
from .models import User

# Create your views here.

def home(request):
    return render(request, "login.html")

def signup(request):

    if request.method == 'POST':
        print(request.POST)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password = request.POST['password']  # Remember to hash the password before saving

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            password=password
        )
        # Redirect to login page or any other page you want
        return redirect('login')
    return render(request, 'signup.html')

def login(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)
            if user.password == password:
                # Successful login
                # You can redirect to the user's dashboard or any other page
                return redirect('dashboard')
            else:
                # Incorrect password
                return render(request, 'login.html', {'error_message': 'Incorrect password'})
        except User.DoesNotExist:
            # User does not exist
            return render(request, 'login.html', {'error_message': 'User does not exist'})

    return render(request, 'login.html')

def dashboard(request):

    return render(request, 'dashboard.html')
