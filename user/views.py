from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import AssessmentForm
from .models import VehicleReport, Assessment
from django.urls import reverse

#Homepage view
def home(request):
    #More logic Leon!
    # Render the index.html template and return it as a response
    return render(request, 'index.html')
    

# User registration view
#@csrf_protect
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # using Django's built-in form for user creation
        if form.is_valid():
            form.save()  # saves the new user record
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # authenticates the new user
            login(request, user)  # logs the user in
            return redirect('user:dashboard')   # redirects to the home page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# User login view
#@login_required# ensures that only authenticated users can access that view.
#@csrf_protect
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)  # using Django's built-in form for authentication
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)  # authenticates the user
            if user is not None:
                login(request, user)  # logs the user in
                return redirect('user:dashboard')  # redirects to the dashboard after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
# User logout view
def logout_view(request):
    logout(request)  # Log the user out
    return redirect('home')  # Redirect to the login page or another desired page
# 
# User profile view
@login_required  # requires the user to be authenticated
def profile(request):
    return render(request, 'profile.html', {'in_dashboard': True})  # returns the profile page

# User dashboard view
@login_required  # requires the user to be authenticated
def dashboard(request):
    # Query the database for vehicle reports submitted by the current user.
    # This assumes that each VehicleReport is linked to a user
    user_vehicle_reports = VehicleReport.objects.filter(submitted_by=request.user)

    # Calculate some additional data to display on the dashboard, for example, the number of reports
    number_of_reports = user_vehicle_reports.count()

    # You can also perform other calculations or obtain additional data as required for your application

    # Prepare the context data to pass to the template
    context = {
        'user_vehicle_reports': user_vehicle_reports,  # list of reports
        'number_of_reports': number_of_reports,  # additional data
        # ... other context data you want to include ...
    }

    # Render the dashboard template with the context data
    return render(request, 'dashboard.html', context)


# Assessment submission view
@login_required  # requires the user to be authenticated
def submit_report(request):
    if request.method == 'POST':
        form = AssessmentForm(request.POST, request.FILES)  # your form for assessment submission, handling files
        if form.is_valid():
            assessment = form.save(commit=False)
            assessment.user = request.user  # sets the user for this assessment
            assessment.save()  # saves the assessment record
            # Here, you might add the logic to send this assessment to your ML model
            return redirect('test_report', assessment_id=None)  # redirects to the results page
    else:
        form = AssessmentForm()
    return render(request, 'submit_report.html', {'form': form,'in_dashboard': True},)

# Assessment past results view
def test_report(request):
    # Your existing code
    return render(request, 'test_report.html', {'in_dashboard': True})
#about
def about(request):
    request.session['visited_dashboard'] = True
    return render(request, 'about.html')  # Render your 'about' page
#contact
def contact(request):
    request.session['visited_dashboard'] = True
    return render(request, 'contact.html')  # Render your 'contact' page

