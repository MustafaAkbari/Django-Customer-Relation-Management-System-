from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist 
from .forms import SignUpForm, AddCustomerForm, AddAddressFrom
from .models import Customer, Address
# Create your views here.

def home(request):
    customers = Customer.objects.all()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Successfuly Logged In.")
            return redirect('home')
        else:
            messages.error(request, "Login Error, Please Try Again!")
            return redirect('home')
    return render(request, 'home.html', {'customers': customers})


def logout_user(request):
    logout(request)
    messages.success(request, "You Have Successfuly Logged Out.")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authentication and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username= username, password= password)
            # login(request, user)
            messages.success(request, "You have successfully registered.")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})

def customer(request, pk):
    if request.user.is_authenticated:
        customer = get_object_or_404(Customer, pk=pk)
        try:
            address = Address.objects.get(pk=pk)
        except ObjectDoesNotExist:
            messages.info(request, "Address of this customer has not asigned yet!")
            return redirect('home')
        else:
            return render(request, 'customer.html', {'customer': customer,
                                                 'address': address})
    else:
        messages.info(request, "You must be logged in to view this page!")
        return render(request, 'home.html', {})

def delete(request, pk):
    if request.user.is_authenticated:
        customer = get_object_or_404(Customer, pk=pk)
        customer.delete()
        messages.success(request, f'Customer named {customer.first_name} deleted!')
        return redirect('home')
    else:
        messages.info(request, "You must be logged in to view this page!")
        return render(request, 'home.html', {})

def add_customer(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddCustomerForm(request.POST)
            if form.is_valid():
                customer = form.save(commit=True)  # Create an instance of the Customer model from meta class of AddCustomerFrom
                messages.success(request, f'Customer named {customer.first_name} saved!')
                return redirect('home')
        else:
            form = AddCustomerForm()
        return render(request, 'add_customer.html', {'form': form})
    else:
        messages.info(request, "You must be logged in to view this page!")
        return render(request, 'home.html', {})
def add_address(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddAddressFrom(request.POST)
            if form.is_valid():
                address = form.save(commit=True)
                messages.success(request, f'Address successfully created for {address.customer}')
                return redirect('home')
        else:
            form = AddAddressFrom()
        return render(request, 'add_address.html', {'form': form})
    else:
        messages.info(request, "You must be logged in to view this page!")
        return render(request, 'home.html', {})

def update_customer(request, pk):
    if request.user.is_authenticated:
        upd_customer = Customer.objects.get(pk=pk)
        if request.method == "POST":
            form = AddCustomerForm(request.POST, instance=upd_customer)
            if form.is_valid():
                form.save()
                messages.success(request, f'Customer successfully updated!')
                return redirect('update-address', pk=pk)
        else:
            form = AddCustomerForm(instance=upd_customer)
        return render(request, 'update_customer.html', {'form': form})
    else:
        messages.info(request, "You must be logged in to view this page!")
        return render(request, 'home.html', {})

def update_address(request, pk):
    if request.user.is_authenticated:
        try:
            upd_address = get_object_or_404(Address, customer_id=pk)
        except Address.DoesNotExist:
            messages.error(request, "Address not found.")
            return redirect('home')

        if request.method == "POST":
            form = AddAddressFrom(request.POST, instance=upd_address)
            if form.is_valid():
                form.save()
                messages.success(request, f'Address successfully updated!')
                return redirect('home')
        else:
            form = AddAddressFrom(instance=upd_address)

        return render(request, 'update_address.html', {'form': form})
    else:
        messages.info(request, "You must be logged in to view this page!")
        return render(request, 'home.html', {})

