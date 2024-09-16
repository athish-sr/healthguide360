from django.contrib.auth.forms import UserCreationForm,AuthenticationForm 
from django.contrib import messages
from django.contrib.auth import logout,authenticate,login
from django.shortcuts import render, redirect,get_object_or_404
from .forms import CustomUserCreationForm
from .models import Medicine,Doctor,Department
from django.contrib.gis.geoip2 import GeoIP2
from django.http import JsonResponse
import json
from .forms import CustomUserCreationForm,ContactForm
from django.core.mail import send_mail

# Create your views here.
def index_view(request):
    username = request.user.username
    departments = Department.objects.all()
    doctors = []  # Default to empty list

    if request.method == 'POST':
        print('hi')
        department_id = request.POST.get('department')
        if department_id:
            doctors = Doctor.objects.filter(department_id=department_id)

    context = {
        'username': username,
        'departments': departments,
        'doctors': doctors
    }

    return render(request, 'index.html', context)


def about_view(request):
    username=request.user.username
    return render(request, 'about.html',{'username':username})
def contact_view(request):
    username=request.user.username
    return render(request, 'contact.html',{'username':username})
def diagnoser_view(request):
    username=request.user.username
    return render(request,'diagnoser.html',{'username':username})
def hospitals_nearby_view(request):
    username=request.user.username
    return render(request,'hospitals-nearby.html',{'username':username})

def login_view(request):
    return render(request,'login.html')
def sign_up_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = CustomUserCreationForm()
    return render(request, 'sign_up.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('/home')  # Redirect to home or another page
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('/home')
def disease_view(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        render(request,'disease.html',{'message':message})
    return render(request,'disease.html')
def mental_view(request):
    return render(request,'mental.html')
def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'medicine.html', {'medicines': medicines})

def search_medicine(request):
    query = request.GET.get('query', '')
    medicines = Medicine.objects.filter(product_name__icontains=query)
    results = list(medicines.values())
    return JsonResponse({'results': results})

def medicine_detail(request, id):
    medicine = get_object_or_404(Medicine, pk=id)
    try:
        drug_interactions = json.loads(medicine.drug_interactions) 
        drug=drug_interactions['drug']
        brand=drug_interactions['brand']
        effect=drug_interactions['effect'] # Convert JSON string to Python dictionary
        combined=zip(drug,brand,effect)
        
    except json.JSONDecodeError:
        combined = {}
    return render(request,'medicine_details.html', {'medicine': medicine,'combined':combined})
def contact_view(request):
    username=request.user.username
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            contact_type = contact.type
            
            # Determine the recipient email and subject based on contact_type
            if contact_type == 'query':
                subject = 'New Query Received'
                recipient_email = 'athishsamy123@gmail.com'
            elif contact_type == 'feedback':
                subject = 'New Feedback Received'
                recipient_email = 'athishsamy123@gmail.com'
            elif contact_type == 'other':
                subject = 'General Inquiry'
                recipient_email = 'athishsamy123@gmail.com'
            else:
                subject = 'Contact Form Submission'
                recipient_email = 'athishsamy123@gmail.com'
            
            # Prepare the email content
            message = f"""
            You have a new {contact_type} from {contact.name}:
            
            Email: {contact.email}
            Phone Number: {contact.phone_no}
            Message: {contact.message}
            """
            e='athish1308@gmail.com'
            print(message)
            # Send email
            send_mail(
                subject,
                message,
                e,  # From email
                [recipient_email],  # To email
                fail_silently=False,
            )
            messages.success(request, 'Message sent successfully!')
            return redirect('contact')  # Adjust to the appropriate URL name or path
        else:
            messages.error(request, 'There was an error with your submission.')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form,'username':username})