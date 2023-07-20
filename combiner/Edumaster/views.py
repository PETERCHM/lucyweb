from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import RegistrationForm
from .models import UserProfile, Payment, Website

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user, country=form.cleaned_data['country'], phone_number=form.cleaned_data['phone_number'])
            login(request, user)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('account')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def account(request):
    user_profile = UserProfile.objects.get(user=request.user)
    payments = Payment.objects.filter(user=request.user)
    websites = Website.objects.all()
    return render(request, 'account.html', {'user_profile': user_profile, 'payments': payments, 'websites': websites})

@login_required
def payment(request, website_id):
    website = Website.objects.get(id=website_id)
    if request.method == 'POST':
        amount = request.POST.get('amount')
        payment_method = request.POST.get('payment_method')
        Payment.objects.create(user=request.user, amount=amount, payment_method=payment_method)
        return redirect('website_access', website_id=website_id)
    return render(request, 'payment.html', {'website': website})

@login_required
def website_access(request, website_id):
    website = Website.objects.get(id=website_id)
    # Perform any additional checks or operations before allowing access
    return render(request, 'website_access.html', {'website': website})
